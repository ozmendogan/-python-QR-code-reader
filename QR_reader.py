import cv2
import numpy as np
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)



cap.set(3,860)
cap.set(4,640)
with open('mydatalist.text') as f:
    mydatalist = f.read().splitlines()

while True :

    success,img = cap.read()
    for barcode in decode(img):


        mydata = barcode.data.decode("utf-8")

        if mydata in mydatalist:
            output = "authorized"
        else:
            output = "not-authorized"

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        print(barcode)
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,output, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 4)


    cv2.imshow("result",img)
    cv2.waitKey(1)
