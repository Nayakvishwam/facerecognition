import cv2
import numpy as np
import os


def identify_faces(model):
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            label, confidence = model.predict(face)

            if confidence < 100:  # Confidence threshold
                name = f"User {label}"
            else:
                name = "Unknown"

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, name, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow("Identifying Faces", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


def train_model():
    # Prepare data
    faces = []
    labels = []

    for user_id in os.listdir('dataset'):
        for image_name in os.listdir(f'dataset/{user_id}'):
            image_path = f'dataset/{user_id}/{image_name}'
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces.append(image)
            labels.append(int(user_id))  # Ensure user_id is an integer

    # Create the model
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(faces, np.array(labels))

    return model