# Gesture-Controlled-White-Board

This project uses the Mediapipe library to perform hand tracking and allows the user to draw on the screen using their hand gestures.

# Setup

## Install the Required Libraries

Before running the project, you need to install the necessary Python libraries. The project dependencies are listed in the `requirements.txt` file. To set up your environment, follow these steps:

1. **Navigate to the Project Directory:**

   Open a terminal or command prompt and navigate to the directory where your Python project is located.

   ```bash
   cd path/to/your/project


2. **Activate Virtual Environment (Optional):**

    If you are using a virtual environment, activate it. If you don't have a virtual environment, you can skip this step.
    
    ```bash
    source venv/bin/activate   # For Linux or macOS
    venv\Scripts\activate      # For Windows


3. **Install Dependencies:**

    Use the following command to install the required libraries listed in the requirements.txt file.
    
    ```bash
    pip install -r requirements.txt
    ```
    
    This will install all the necessary libraries along with their specific versions.

4. **Run the Project:**

    Now that the dependencies are installed, you can run the project using the main Python file. Use the following command:
    
    ```bash
    python main.py
    ```
    This will start the hand-tracking application.
    

---

# Features and Controls

- **Drawing Mode :**
  In Drawing Mode, users can create freehand drawings on the screen by moving their index finger.
  
  **Usage Instructions :**
  1. Extend the index finger and move it on the screen to draw lines.
     
     ![drawing mode](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/1e458238-c3e4-4970-8d7b-128dd52dc9d7)
     
---

- **Selection Mode :**
   Selection Mode enhances the user experience by allowing them to interact with the drawing environment in a non-drawing capacity. Instead of creating lines,          users can perform specific gestures to select colors from the palette and access other features. Selection Mode provides a seamless way for users to interact       with the drawing environment without leaving unintentional marks. 
   
   **Usage Instructions:**
   1. Color Selection: Raise the index finger and the thumb pointing towards the outer direction. Hover them over the color palette and drawing color will change        accordingly.
      ![color selection](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/a8bad976-2d06-47a5-907e-aee08153cef6)

   2. Clear All: Hover Guesture over the "Clear All" button and close the open the thumb (like a click) to clear the entire canvas and start anew.
      ![clear all click1](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/a85f355f-8941-40f7-99c6-5ea14b35c43b)
      ![clear all click2](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/ae5767ed-783e-4fcb-a151-1a97d6ce84b2)
      
---

- **Pen Thickness Adjustment :**
  The Pen Thickness Adjustment feature enriches the drawing experience by allowing users to dynamically control the thickness of the lines they draw.
  The system provides visual feedback by displaying a dynamic pointer that represents the current thickness of the pen.

   **Usage Instructions:**
   1. Gesture: Raise the index finger thumb and the pinky finger towards the outer direction.
   2. Size Control: Move the gesture UP to Increase the thickness and DOWN to Decrease the thickness of the pen.
      ![resize pen1](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/165edcc2-28b4-45e7-b6ae-b6688d756284)
      ![resize pen2](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/cb8a249d-090f-4c8d-9746-91496f03e31f)
      
---
   
- **Eraser Mode :**
  The Eraser Mode provides users with a convenient way to correct or remove specific parts of their drawings.The system provides visual cues, such as a dynamic eraser circle, to indicate the current size and position of the eraser.

  **Usage Instructions(Erasing):**
   1. Gesture: Make a Fist.
   2. Control: Move the gesture(fist) over the areas you want to erase.
      
      ![eraser](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/aaa78c7f-8ddb-4fca-b7e7-b8b2116bbaa9)


   **Usage Instructions(Eraser Size):**
   1. Gesture: Make a Fist with thumb pointing towards outward direction.
   2. Size Control: Move the gesture(fist) DOWN to Increase the size of Eraser and UP to Decrease teh size of Eraser.
      
      ![eraser size1](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/972f9da8-9cf8-4058-89b4-6e96ab19bc26)
      ![eraser size2](https://github.com/Kaustic-user/Gesture-Controlled-White-Board/assets/118257539/45832d8a-cbc7-4aeb-a8cb-1eaeefa30d95)

---

**Note:** Ensure proper lighting conditions for accurate hand tracking, and have fun expressing your creativity through gestures!
   
