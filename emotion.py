import cv2
import threading

emotion_score = 0
running = False

def emotion_worker():

    global emotion_score, running

    cam = cv2.VideoCapture(0)

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    total_frames = 0
    face_frames = 0

    while running:

        ret, frame = cam.read()
        if not ret:
            break

        total_frames += 1

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            face_frames += 1

        for (x,y,w,h) in faces:

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.putText(
                frame,
                "Emotion Tracking",
                (x,y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2
            )

        cv2.imshow("Interview Emotion Detection",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    if total_frames == 0:
        emotion_score = 0
    else:
        emotion_score = int((face_frames/total_frames)*100)


def start_emotion_detection():

    global running

    running = True

    thread = threading.Thread(target=emotion_worker)
    thread.start()


def stop_emotion_detection():

    global running
    running = False


def get_emotion_score():
    return emotion_score