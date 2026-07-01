import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("models/best.pt")

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("AI Pothole Detection", annotated)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()