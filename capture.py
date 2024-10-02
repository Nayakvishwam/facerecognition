import cv2
import os

def capture_faces(user_id):
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    count = 0
    os.makedirs(f"dataset/{user_id}", exist_ok=True)

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"dataset/{user_id}/face_{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Capturing Faces", frame)

        if count >= 30:  # Capture 30 images per user
            break

    cam.release()
    cv2.destroyAllWindows()