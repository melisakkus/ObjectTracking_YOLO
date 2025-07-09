# import os
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'  # KMP_DUPLICATE_LIB_OK hatasını önlemek için

import cv2
import imutils 
from ultralytics import YOLO 
import numpy as np

video_path="tekvagon.mp4"
cap = cv2.VideoCapture(video_path)

model_name = "yolov8n.pt"
model = YOLO(model_name)

person_id = 0

while True:
    ret, frame=cap.read()
    if ret == False:
        break

    frame = imutils.resize(frame, width=1200) 

    results = model.track(frame,persist=True,verbose = False)[0]

    bboxes = np.array(results.boxes.data.tolist(), dtype="int")

    for box in bboxes:
        x1,y1,x2,y2,track_id,score,class_id = box

        if class_id == person_id:
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = "ID:{} PERSON". format(track_id)
            cv2.putText(frame,text,(x1,y1-5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    cv2.imshow("Object Tracking",frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()