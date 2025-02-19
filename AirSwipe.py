import cv2 as cv
import mediapipe as mp
from pyautogui import press
from time import sleep

# Initialize MediaPipe Hand Detection
Hand = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
Draw = mp.solutions.drawing_utils

# Flags & Thresholds
DRAW_HAND = True  # Set to True if you want landmarks drawn
MOVEMENT_THRESHOLD = 0.2  

# Variables to Track Movement
prev_x8, prev_y8 = 0.0, 0.0

cap = cv.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Camera not initialized")
        break

    img = cv.flip(img, 1)
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = Hand.process(rgb_img)

    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            if DRAW_HAND:
                Draw.draw_landmarks(img, hand_landmark, mp.solutions.hands.HAND_CONNECTIONS)

            # Track index finger tip (landmark 8)
            curr_x8, curr_y8 = hand_landmark.landmark[8].x, hand_landmark.landmark[8].y

            # Calculate movement
            delta_x = curr_x8 - prev_x8
            delta_y = curr_y8 - prev_y8

            # Check if index finger is above middle finger
            if hand_landmark.landmark[8].y < hand_landmark.landmark[7].y:
                if delta_x > MOVEMENT_THRESHOLD:
                    press('right')
                    print("RIGHT")
                    sleep(0.3)

                elif delta_x < -MOVEMENT_THRESHOLD:
                    press('left')
                    print("LEFT")
                    sleep(0.3)

            # Update previous position
            prev_x8, prev_y8 = curr_x8, curr_y8

    cv.imshow("Feed", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
