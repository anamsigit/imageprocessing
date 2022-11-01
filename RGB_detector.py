'''
RGB memiliki tigak komponen warna dasar, yakni red (merah), green (hijau), dan blue (biru). 
RGB menggunakan kombinasi tiga warna primer tersebut untuk menghasilkan warna-warna lainnya. 
HSV adalah model warna yang berasal dari hasil transformasi non linier dari warna primer.
'''

#https://pysource.com/2021/10/19/simple-color-recognition-with-opencv-and-python/
import cv2
import numpy as np

cap = cv2.VideoCapture(0) #value ini berisi webcam mana yang anda pilih, isi 0 untuk menggunakan kamera bawaan laptop
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    # hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)


    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    print( b, g, r)

    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    # --------------->
    start_point = (5, 5)
    end_point = (220, 220)
    color = (b, g, r)
    thickness = -1
    cv2.rectangle(frame, start_point, end_point, color, thickness)
    #---------------->
    lower_color = np.array([0, 0, 200], dtype = "uint8") 
    upper_color = np.array([0, 0, 255], dtype = "uint8")
    mask = cv2.inRange(frame, lower_color, upper_color)
    cv2.imshow("red color detection", mask) 

    

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()