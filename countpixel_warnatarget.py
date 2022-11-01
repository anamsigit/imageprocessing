import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

while 1:
	ret,frame =cap.read()
	# ret will return a true value if the frame exists otherwise False
	into_hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	# changing the color format from BGr to HSV
	# This will be used to create the mask
	L_limit=np.array([98,50,50]) # setting the blue lower limit
	U_limit=np.array([139,255,255]) # setting the blue upper limit
	# L_limit=np.array([98,50,50]) # setting the blue lower limit
	# U_limit=np.array([139,255,255]) # setting the blue upper limit
		

	b_mask=cv2.inRange(into_hsv,L_limit,U_limit)
	# creating the mask using inRange() function
	# this will produce an image where the color of the objects
	# falling in the range will turn white and rest will be black
	blueframe=cv2.bitwise_and(frame,frame,mask=b_mask)
	totalpixel = blueframe.size
	countpixeltarget = np.count_nonzero(blueframe)
	percentage = round(countpixeltarget * 100 / totalpixel, 2)
	print(percentage)

#------------------------------

	px=frame[300,300]
	# print(px)
	warnatarget=frame[300,300,0]
	warnatarget2 = frame[100,100,0]
	# print(warnatarget2)
#-----------------------------
	# b = blue[:, :, :1]
	# g = blue[:, :, 1:2]
	# r = blue[:, :, 2:]

	# # computing the mean
	# b_mean = np.mean(b)
	# g_mean = np.mean(g)
	# r_mean = np.mean(r)

	# # displaying the most prominent color
	# if (b_mean > g_mean and b_mean > r_mean):
	# 	print("Blue")
	# if (g_mean > r_mean and g_mean > b_mean):
	# 	print("Green")
	# else:
	# 	print("Red")
	

	# center_coordinates = (300, 300)
	# radius = 2
	# color = (300,300,0)
	# thickness = 2
	# cv2.circle(blueframe, center_coordinates, radius, color, thickness)

	


	# this will give the color to mask.
	cv2.imshow('Original',frame) # to display the original frame
	cv2.imshow('Blue Detector',blueframe) # to display the blue object output

	if cv2.waitKey(1)==27:
		break
	# this function will be triggered when the ESC key is pressed
	# and the while loop will terminate and so will the program
cap.release()

cv2.destroyAllWindows()

# importing required libraries
import cv2
import numpy as np

# taking the input from webcam
vid = cv2.VideoCapture(0)

# running while loop just to make sure that
# our program keep running until we stop it


	# setting values for base colors

# import sys
# import numpy as np
# import cv2
 
# blue = sys.argv[1]
# green = sys.argv[2]
# red = sys.argv[3]  
 
# color = np.uint8([[[blue, green, red]]])
# hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
 
# hue = hsv_color[0][0][0]
 
# print("Lower bound is :"),
# print("[" + str(hue-10) + ", 100, 100]\n")
 
# print("Upper bound is :"),
# print("[" + str(hue + 10) + ", 255, 255]")