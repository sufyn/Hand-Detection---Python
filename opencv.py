import cv2
import mediapipe as mp
mp_drawings=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands
cam=cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
    while cam.isOpened():
        ret, frame=cam.read(-1)
  
        image=cv2.cvtColor( frame, cv2.COLOR_BGR2RGB)
        image=cv2.flip(image,1)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        print(results)
        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawings.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS)
                mp_drawings.DrawingSpec(color=(121,22,76),thickness=2,circle_radius=4)
                mp_drawings.DrawingSpec(color=(250,44,250),thickness=2,circle_radius=2)
        cv2.imshow("handTracking",image)
        if cv2.waitKey(1)==ord('q'):
            break
cam.release()
cv2.destroyAllWindows()




