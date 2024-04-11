from ultralytics import YOLO
model = YOLO('yolov8s.pt')
results = model.train(data=r"C:\Users\bhatt\Desktop\samir patel paper\potholes\data.yaml",epochs=16)


