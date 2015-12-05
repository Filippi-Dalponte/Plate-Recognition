#finestra che mostra il video in diretta con evidenziato eventuale riconoscimento


import cv2
import urllib
import numpy as np
import ctypes
from ftplib import FTP
import time

x1=0
x2=0
x3=0
x4=0
y1=0
y2=8
y3=0
y4=0
immx=0
immy=0
immx1=500
immy1=500
tempopresente=0
tempopassato=0
valstanga=0



stream=urllib.urlopen('http://192.168.0.44:8080/video')
ftp = FTP('192.168.0.44', 'bananapi', 'bananapi', timeout=2)
    

bytes=''
while True:
    tempopresente=time.time()
    if (tempopresente-tempopassato)>0.2:
        tempopassato=tempopresente
        
        try:
            temp=open('temp.conf','w')
            ftp.retrbinary('RETR /home/bananapi/Desktop/trasmissione.conf', temp.writelines)
            temp.close()
            f = open('temp.conf','r')
            trasm=eval(f.read())  

            user32 = ctypes.windll.user32
            Yval=int(user32.GetSystemMetrics(1)*0.66)        
            rapp_trasf=((user32.GetSystemMetrics(1)*0.66)/(eval(trasm['immy'])))
            Xval=int((eval(trasm['immx']))*rapp_trasf)            
        
            targa=trasm['targa']
            x1=int((eval(trasm['x1']))*rapp_trasf)
            y1=int((eval(trasm['y1']))*rapp_trasf)
            x2=int((eval(trasm['x2']))*rapp_trasf)
            y2=int((eval(trasm['y2']))*rapp_trasf)
            x3=int((eval(trasm['x3']))*rapp_trasf)
            y3=int((eval(trasm['y3']))*rapp_trasf)
            x4=int((eval(trasm['x4']))*rapp_trasf)
            y4=int((eval(trasm['y4']))*rapp_trasf)
            immx=int((eval(trasm['immx']))*rapp_trasf)
            immy=int((eval(trasm['immy']))*rapp_trasf)
            valstanga=(trasm['valstanga'])            
          
        except:
            pass       
       
    
    bytes=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        
        ridimensiona=cv2.resize(i, (Xval,Yval), fx=5, fy=5)
        
        pts = np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]], np.int32)
        
        if valstanga==0:
            cv2.polylines(ridimensiona,[pts],True,(0,0,255),2)
        else:
            cv2.polylines(ridimensiona,[pts],True,(0,255,0),2)
        
        cv2.putText(ridimensiona,targa, (x1,y1-5), cv2.FONT_HERSHEY_PLAIN, 1.2,(255,255,255),2)
        cv2.putText(ridimensiona,"Q=Uscita", (0,20), cv2.FONT_HERSHEY_PLAIN, 1.2,(255,255,255),2)
        
        
        cv2.imshow("Riconoscimento targhe",ridimensiona)        
               
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            

cv2.destroyAllWindows()
