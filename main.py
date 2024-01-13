import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open the camera with the desired resolution
cap = cv2.VideoCapture(0)
width, height = 1280, 720   # Adjust these values based on your preference
cap.set(3, width)   # Set the width of the frame
cap.set(4, height)  # Set the height of the frame

depth = 501

# Variables to store the initial hand position and previous index finger tip position
initial_hand_landmarks = None

# Initialize drawing parameters
base_for_pen_size = None
flag_pen = 0
drawing_color = (255, 0, 0)  # Blue color for drawing
drawing_thickness = 10  # Adjust as needed
drawing = False
drawn_lines = []  #tuple of 3[start coordinate ,end coordinate ,color] (list of tuples)

color_palette = [
    (255, 0, 0),    # Blue
    (0, 255, 0),    # Green
    (0, 0, 255),    # Red
    (0, 255, 255),  # Yellow
    (255, 255, 255),  # White
    (0, 0, 0),      # Black
]

color_palette_radius = 20

base_for_eraser_size = None
eraser_radius = 20 #Default eraser radius

top_boundary = 70 #y-coordinate


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Set the background color
    background_color = (230, 216, 173)
    cv2.rectangle(frame, (0, 0), (width, 70), background_color, -1)

    # Draws Color Palette on top of the frame
    for i, color in enumerate(color_palette):
        center = ((i + 0.5) * (width/2) / len(color_palette), 30)      
        cv2.circle(frame, (int(center[0]), int(center[1])), color_palette_radius, color, -1)

    # 'Clear All' button
    cv2.putText(frame, "Clear All", (width - 600, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Current Selected Color
    color_idx = color_palette.index(drawing_color)
    curr_color_center = ((color_idx + 0.5) * (width/2) / len(color_palette), 30) 
    center_point = (int(curr_color_center[0]), int(curr_color_center[1]))

    #Outline on the selected color
    cv2.circle(frame, center_point, color_palette_radius+3, drawing_color, 2) 


    # Check if hands are found
    if results.multi_hand_landmarks:
        # Access landmarks of the first hand
        hand_landmarks = results.multi_hand_landmarks[0]

        # Draws landmarks on the frame
        # mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        
        fingers = []    #Array for storing orientation of fingers (1 = open , 0 = closed)
        for i in range(1, 6):  
            tip_index = i * 4
            base_index = tip_index - 2

            if tip_index == 4:  
                #Compare x coordinate for the thumb
                if hand_landmarks.landmark[tip_index].x < hand_landmarks.landmark[base_index].x:
                    fingers.append(1)  # thumb is open
                else:
                    fingers.append(0)  # thumb is closed

            else:    
                # Compare y-coordinates for the 4 fingers
                if hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[base_index].y:
                    fingers.append(1)  # Finger is open
                else:
                    fingers.append(0)  # Finger is closed
            

        # print("Finger Array:", fingers)

        # Extract index finger tip coordinates (Landmark 8)
        index_finger_tip = (
            int(hand_landmarks.landmark[8].x * width),
            int(hand_landmarks.landmark[8].y * height)
        )
        
####### Drawing Mode ####################################################################################################################
        if fingers == [0,1,0,0,0]:
            # Rectangle coordinates (top-left and bottom-right points)
            rect_top_left = (width - 610, 10)
            rect_bottom_right = (width - 440, 50)

            #Showing the pointer
            cv2.circle(frame, index_finger_tip, int(drawing_thickness/2), drawing_color, 2)

            # Checking if index finger on 'Clear All'
            if (rect_top_left[0] <= index_finger_tip[0] <= rect_bottom_right[0]) and (rect_top_left[1] <= index_finger_tip[1] <= rect_bottom_right[1]):
                drawn_lines = [] #clear the drawn lines is 'Clear All' is pressed

            # Check if the index finger tip is below the top border
            if(top_boundary +(drawing_thickness/2) <= index_finger_tip[1]):
                # Draw along the line of the index finger
                if initial_hand_landmarks is not None:
                    cv2.line(frame, initial_hand_landmarks, index_finger_tip, drawing_color, drawing_thickness)
                    drawn_lines.append((initial_hand_landmarks, index_finger_tip, drawing_color, drawing_thickness))

                # Update initial hand landmarks for the next frame
                initial_hand_landmarks = index_finger_tip

            # Refresh the base for adjusting eraser size
            eraser_radius = 20
            base_for_eraser_size = None

            # base_for_pen_size = None
            flag_pen = 0

####### Selection Mode #####################################################################################################################
        elif fingers == [1,1,0,0,0]:
            initial_hand_landmarks = None  # Ensures we can break between lines

            #Showing the pointer
            cv2.circle(frame, index_finger_tip, int(drawing_thickness/2), drawing_color, 2)
            
            # Selection of drawing color from the Color Palette
            for i, color in enumerate(color_palette):
                center = ((i + 0.5) * (width/2) / len(color_palette), 30)   
                point = index_finger_tip
                distance = np.sqrt((int(center[0]) - point[0])**2 + (int(center[1]) - point[1])**2)

                #Checking if index finger pointing to any color palette color
                if distance <= color_palette_radius:
                    drawing_color = color 

            # Displaying border to the 'Clear All' text
            cv2.rectangle(frame, (width - 610, 10), (width - 440, 50), (0, 0, 0), 2, cv2.LINE_4, 0)

            # Refresh the base for adjusting eraser size
            eraser_radius = 20
            base_for_eraser_size = None

            # base_for_pen_size = None
            flag_pen = 0

####### Adjusting the thickness of the Pen #################################################################################################
        elif fingers == [1,1,0,0,1]:
            # index_finger_tip_z_also = (
            #     int(hand_landmarks.landmark[8].x * width),
            #     int(hand_landmarks.landmark[8].y * height),
            #     int(hand_landmarks.landmark[8].z * depth)  # Replace 'depth' with the appropriate value
            # )

            if flag_pen == 0:
                base_for_pen_size = index_finger_tip


            # Calculate vertical movement of base and index finger tip
            inside_movement =  base_for_pen_size[1] - index_finger_tip[1]

            # Update eraser radius based on vertical movement
            drawing_thickness = min(110,max(5 ,inside_movement))
            # print(drawing_thickness)

            # Draw the pointer
            cv2.circle(frame, index_finger_tip, int(drawing_thickness/2), drawing_color, 2)

            flag_pen = 1



####### Eraser Mode (Note : Eraser located on index finger tip) ###########################################################################
        elif fingers == [1, 0, 0, 0, 0] or fingers == [0, 0, 0, 0, 0]:  # erase(fist)
         
            # Draw eraser circle
            cv2.circle(frame, index_finger_tip, eraser_radius, (255, 255, 255), 1)  # outer circle (white border)
            cv2.circle(frame, index_finger_tip, eraser_radius - 2, (255, 255, 255), -1)  # inner circle (translucent inside)

            # Adjusting the size of eraser ####################
            if fingers == [1, 0, 0, 0, 0]: 

                if base_for_eraser_size is None:
                    base_for_eraser_size = index_finger_tip

                # Calculate vertical movement of base and index finger tip
                vertical_movement = index_finger_tip[1] - base_for_eraser_size[1]

                # Update eraser radius based on vertical movement
                if vertical_movement > 0:
                    eraser_radius = min(140, max(1, 20 + vertical_movement // 3))
                    # print(eraser_radius)

            # Erasing Operation ###############################
            else: 
                # cv2.putText(frame, "Fist Detected", (20, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) # message 

                # Retaining on those lines which are not lieing inside the Eraser's Area
                drawn_lines = [
                    (start, end, color, thickness) for start, end, color, thickness in drawn_lines
                    if (
                        np.linalg.norm(np.array(start) - np.array(index_finger_tip)) > eraser_radius
                        and np.linalg.norm(np.array(end) - np.array(index_finger_tip)) > eraser_radius
                    )
                ]

                # Refresh the base for adjusting eraser size
                base_for_eraser_size = None
            
                # base_for_pen_size = None
                flag_pen = 0
            

#### Draw previously drawn lines on each frame #############################################################################################
    for line in drawn_lines:
        #line[0] = start coordinate
        #line[2] = end coordinate
        #line[2] = drawing color (tuple)
        #line[3] = drawing_thickness
        cv2.line(frame, line[0], line[1], line[2], line[3]) 

    # Display the frame
    cv2.imshow("Hand Tracking", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()


