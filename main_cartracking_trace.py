# import os
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'  # KMP_DUPLICATE_LIB_OK hatasını önlemek için

import cv2
import imutils 
from ultralytics import YOLO 
import numpy as np
from collections import defaultdict

video_path="test.mp4"
cap = cv2.VideoCapture(video_path)

model_name = "yolov8n.pt"
model = YOLO(model_name)

vehicle_id = 2

track_history = defaultdict(lambda: [])

while True:
    ret, frame=cap.read()
    if ret == False:
        break

    frame = imutils.resize(frame, width=1200) 

    #verbose = false her işlemede bize bilgi dönemesini önlüyoruz, 
    #[0] ilk classı döner
    results = model.track(frame,persist=True,verbose = False)[0]

    #nesnelerin konumlarını alalım, gelen değerleri int tipine çevirelim,  2.2 gibi bir değer gelirse
    #bunu 2 olarak alırız, yani tam sayıya çevirir. frame üzerinde çizim yapabilmek için opencv kütüphanesinde metotlar int kabul ediyorlar
    bboxes = np.array(results.boxes.data.tolist(), dtype="int")

    for box in bboxes:
        x1,y1,x2,y2,track_id,score,class_id = box
        
        #kuyruk için
        cx = int((x1+x2)/2)
        cy = int((y1+y2)/2)

        if class_id == vehicle_id:
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = "ID:{} CAR". format(track_id)
            cv2.putText(frame,text,(x1,y1-5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            track = track_history[track_id]
            track.append((cx, cy))
            if len(track) > 40:
                track.pop(0)
            
            points = np.hstack(track).astype("int32").reshape((-1,1,2))
            cv2.polylines(frame, [points], isClosed=False, color=(0, 255, 0), thickness=2)
            

    cv2.imshow("Object Tracking",frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()