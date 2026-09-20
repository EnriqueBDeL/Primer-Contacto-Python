from pathlib import Path
import cv2

base_dir = Path(__file__).resolve().parent
cascade_path = base_dir / 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(str(cascade_path))

if face_cascade.empty():
    raise FileNotFoundError(f'No se pudo cargar el clasificador: {cascade_path}')

cap = cv2.VideoCapture(0)

window_name = 'Deteccion Facial en Tiempo Real'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

is_fullscreen = False

while True:
    success, img = cap.read()

    if not success:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow(window_name, img)

    key = cv2.waitKey(30) & 0xFF

    if key == 27:
        break

    if key in (ord('f'), ord('F')):
        is_fullscreen = not is_fullscreen
        mode = cv2.WINDOW_FULLSCREEN if is_fullscreen else cv2.WINDOW_NORMAL
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, mode)

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()