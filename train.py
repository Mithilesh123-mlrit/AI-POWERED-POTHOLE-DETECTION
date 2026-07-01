from ultralytics import YOLO

# Load pretrained YOLOv8 model
model = YOLO("yolov8n.pt")

# Train model
model.train(
    data="dataset.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="pothole_detector"
)

# Validate
metrics = model.val()

print(metrics)