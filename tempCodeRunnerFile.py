

import cv2
import mediapipe as mp

class GestureController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open video capture device.")
            exit()
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands()

    def start(self):
        while True:
            success, image = self.cap.read()
            if not success:
                print("Error: Failed to capture image.")
                break
            
            # Convert the BGR image to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Process the image and find hands
            results = self.hands.process(image_rgb)
            
            # Draw hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # Your gesture handling code here
                gest_name = handmajor.get_gesture()
                Controller.handle_controls(gest_name, handmajor.hand_result)
            else:
                Controller.prev_hand = None
            
            # Display the image
            cv2.imshow('Gesture Controller', image)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Assuming handmajor and Controller are defined elsewhere in your code
gc1 = GestureController()
gc1.start()
