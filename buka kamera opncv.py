#Import Library OpenCV
import cv2

#Variable untuk VideoCapture
kapture = cv2.VideoCapture(0)

#Fungsi untuk membuat frame pengaturan pada video
while(True):
    #Membaca video 
    #Ret merupakan sebuah boolean (True or False). 
    #Ret mengembalikan nilai True apabila frame berhasil di-capture dan sebaliknya
    #apabila terdapat error pada saat inisiasi proses streaming video tersebut.
    ret, frame = kapture.read()
    #Menampilkan video
    cv2.imshow('frame',frame)

    #Pengaturan frame __ tekan key 'q' untuk menutup frame. anda tidak akan bisa
    #menutupnya dengan hanya memencet silang maka diberi kondisi break ini

    if cv2.waitKey(1) == ord('q'):
        break
kapture.release()
cv2.destroyAllWindows()