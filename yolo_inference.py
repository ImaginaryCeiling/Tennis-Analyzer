from ultralytics import YOLO
 
model = YOLO('yolov8x.pt')

model.track('input_files/input_video.mp4', conf=0.2, save  = True)
