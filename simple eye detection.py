import cv2
from simple_pid import PID

# Enable camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 420)

eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")


while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # detecting eyes
    eyes = eyeCascade.detectMultiScale(imgGray)

    # drawing bounding box for eyes
    for (ex, ey, ew, eh) in eyes:
        img = cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 3)

        xCentersatu = ((ex+ew) + ex ) /2
        yCentersatu = ((ey+eh) + ey) /2

        # center_coordinates = (int(xCenter), int(yCenter)) #pengubahan float menjadi int, menjadikan data tidak akurat 0.5
        center_coordinatesatu = (int(xCentersatu), int(yCentersatu))
        radius = 30
        thickness = -1
        cv2.circle(img, center_coordinatesatu, radius, thickness)

    
    cv2.imshow('face_detect', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyWindow('face_detect')