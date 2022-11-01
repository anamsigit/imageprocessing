#jika tidak bisa membuat baris baru, gunakan alt + shift + panah saja


#OPENCV
from collections import deque
from turtle import update
import numpy as np
import argparse
import imutils
import cv2


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (98,50,50)
greenUpper = (139,255,255)
# greenLower = (0, 0, 0)
# greenUpper = (0, 0, 0)

redLower = (133, 54, 99)
redUpper = (255, 255, 255)

pts = deque(maxlen=args["buffer"])

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])



#PID
from cv2 import CascadeClassifier as CC
from simple_pid import PID
import json

# koorpenyimpanganjalurx = 23 #start dimana koordinat menyimpang dari nilai koordinat jalur yang benar
# koorpenyimpanganjalury = 60



ujisifat = [] #menguji apakah sebuah algoritma while dapat menyimpan suatu nilai ke list secara kontinu : jawabanya bisa asalakan sebagai file yang dijalankan
logPIDpoint = []


# nilaix = {'evaluasi': koorpenyimpanganjalurx} #variabel menyimpan koordinat terkini yang seiring akan dikurang setiap satuan waktu oleh nilaix.update
# nilaiy = {'evaluasi': koorpenyimpanganjalury}


def pidcontrolx(errorx):
    pidx = PID(0.25, 0.007, 0.0066, setpointx, sample_time=0.5) #satu fungsi hanya berlaku untuk 1 error, tidak bisa multi

    koreksix = pidx(errorx)

    if errorx == setpointx:
        print(errorx,'==',setpointx,'koordinat x dalam jalur yang benar')
        evaluasi = errorx + koreksix #disinlah letak pengurangan error oleh koreksi
    else:
        print(errorx, "akan dikurangi sebanyak", koreksix, "setiap satuan waktu hingga diperoleh nilai", setpointx)
        evaluasi = errorx + koreksix
        
    return evaluasi

def pidcontroly(errory):
    pidy = PID(0.25, 0.007, 0.0066 , setpointy, sample_time=0.5) #satu fungsi hanya berlaku untuk 1 error, tidak bisa multi

    koreksiy = pidy(errory) #pid menghitung kesalahan

    if errory == setpointy:
        print(errory,'==',setpointy,'koordinat y dalam jalur yang benar')
        evaluasi = errory + koreksiy #disinlah letak pengurangan error oleh koreksi

    else:
        print(errory, "akan dikurangi sebanyak", koreksiy, "setiap satuan waktu hingga diperoleh nilai", setpointy)
        evaluasi = errory + koreksiy

    return evaluasi


# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break

	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask

	# mask1 = cv2.inRange(hsv, greenLower, greenUpper)
	# mask1 = cv2.erode(mask1, None, iterations=2)
	# mask1 = cv2.dilate(mask1, None, iterations=2)

	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	mask2 = cv2.inRange(hsv, redLower, redUpper)
	mask2 = cv2.erode(mask2, None, iterations=2)
	mask2 = cv2.dilate(mask2, None, iterations=2)

	# mask2 = cv2.inRange(hsv, redLower, redUpper)
	# mask2 = cv2.erode(mask2, None, iterations=2)
	# mask2 = cv2.dilate(mask2, None, iterations=2)

	# mask = cv2.bitwise_or(mask1, mask2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	cnts2 = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0 and len(cnts2) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		c2 = max(cnts2, key=cv2.contourArea)

		((x, y), radius) = cv2.minEnclosingCircle(c)
		((x2, y2), radius2) = cv2.minEnclosingCircle(c2)

		M = cv2.moments(c)
		M2 = cv2.moments(c2)

		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

			cv2.circle(frame, (int(x2), int(y2)), int(radius2), (0, 255, 255), 2)
			cv2.circle(frame, center2, 5, (0, 0, 255), -1) #memberikan titik tengah

			# cv2.line(frame, (int(x), int(y)), (int(x2), int(y2)), (0, 0, 255), 1) #yang atas dan bawah sama aja
			cv2.line(frame, center, center2, (0, 0, 255), 1)

			#PID
			tengahx = int((int(x)+int(x2))/2)
			tengahy = int((int(y)+int(y2))/2)

			tengahx = int((center[0]+center2[0])/2)
			tengahy = int((center[1]+center2[1])/2)

			setpointx = tengahx
			setpointy = tengahy
			

			with open('D:\dokumen\Academic\Pemograman\python\Library OpenCV\PIDpoint.json', 'r') as baca:
				data = json.load(baca)
			
			intnilaix = int(float(data['evaluasix']))
			intnilaiy = int(float(data['evaluasiy']))

			PIDpoint = {
				"evaluasix": f"{pidcontrolx(intnilaix)}",
				"evaluasiy": f"{pidcontroly(intnilaiy)}"
			}
			
			with open("D:\dokumen\Academic\Pemograman\python\Library OpenCV\PIDpoint.json", 'w') as tulis:
				json.dump(PIDpoint, tulis)
				

	
			with open('D:\dokumen\Academic\Pemograman\python\Library OpenCV\PIDpoint.json', 'r') as baca:
				data = json.load(baca)


			updatednilaix = int(float(data['evaluasix']))
			updatednilaiy = int(float(data['evaluasiy']))

			logPIDpoint.append(updatednilaix)

			koordinatPID = int(updatednilaix), int(updatednilaiy)

			# cv2.circle(frame, (434, 3434), int(radius2), (0, 255, 255), 2) #argumen fungsi PID harus dinamis nilainya, cobalah dengan nilai statis dulu untuk pemahaman
			cv2.circle(frame, (koordinatPID), int(15), (30, 154, 70), -1)
			ujisifat.append(1)
			print('jumlahnya apakah kontinuuuuuuu',len(ujisifat))

        
       

            


	# update the points queue
	# pts.appendleft(center) ini berguna untuk membuat jejak

	# loop over the set of tracked points
	# for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		# if pts[i - 1] is None or pts[i] is None:
		# 	continue

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		# thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		# cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		# buat log
		with open("D:\dokumen\Academic\Pemograman\python\Library OpenCV\logPIDpoint.json", 'w') as tulis:
			json.dump(logPIDpoint, tulis)
		print('log saved to', "D:\dokumen\Academic\Pemograman\python\Library OpenCV\logPIDpoint.json" )
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
print('selesai')