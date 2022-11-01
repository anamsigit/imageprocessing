#import opencv
import cv2
#import numpy
import numpy

#fungsi lingkaran
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #fungsi lingkaran
        cv2.circle(img,(x,y),10,(0,0,255), -1) #KETIKA MOUSE DIPENCET AKAN MENGHASILKAN GARIS LINGKARAN
        print('koor x : ',x)
        print('koor y : ',y)
        #fungsi kotak
        #cv2.rectangle(img,(x,y),(x+200,y+200), (255,0,0),3) #KETIKA MOUSE DIPENCET AKAN MENGHASILKAN TULISAN GARIS KOTAK
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img,'ivanjul.com',(x,y),font,2,(255,0,0),3)  #KETIKA MOUSE DIPENCET AKAN MENGHASILKAN TULISAN IVANJUL.COM

#Fungsi gambar hitam
img = numpy.zeros((512,512,3), numpy.uint8)
cv2.namedWindow('image')

#fungsi mousecallback -> ini adalah inti dari mouse interaktif, ini akan memanggil fungsi draw_circle yang dibuat diatas
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) == ord('q'): #jika anda meningkatkan parameter di waitkey, mungkin anda tidak cukup menekan q untuk keluar dengan mudah
        break
cv2.destroyAllWindows