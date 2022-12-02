#Python Imageprocessing
python imageprocessing

this repository contains separate executable files, except for those associated with PIDpoint.json and logPIDpoint.json

some brief explanation about python files
1. RGB detector: detects the color of a predetermined 1 pixel on a screen.
2. arduino_logPIDpoint : this file is actually a log result from my research on YOLOX, where arduino with python will run the servo according to the recorded coordinates.
3. ball tracker - PID Controler JSON : detects objects in the form of red and green circles, by implementing a PID controller and storing them in a JSON file (which I said earlier)
4. ball tracker - Arduino PID Controller: almost similar to the 3rd file but here I directly connect it to Arduino
5. ball tracker - PID Controller: not much different from files 4 and 3
6. countpixel_warnatarget : counts the total of certain pixels in a frame
7. interactive mouse: using the tkinter module, with this file, you will easily determine the coordinates of a screen
8. oepncamera_opencv : basic code for the opencv module to open the camera, select index camera to choose which camera you want to open using the opencv module
9. simple eye detection: opencv module that can detect eyes

anamsigit
Yogyakarta, 29 November 2022
