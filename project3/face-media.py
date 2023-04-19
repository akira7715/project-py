import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    with mp_face_detection .FaceDetection(min_detection_confidence=0.5) as face_detection :
        results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # 顔検出結果の描画
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(img, detection)
    
    img = cv2.flip(img, 1)
    cv2.imshow('frame',img)
    key = cv2.waitKey(1)
    if key == ord("q") or key == ord("Q"):
        break
