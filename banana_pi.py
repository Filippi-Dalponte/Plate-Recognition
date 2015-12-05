#programma eseguito a bordo della scheda Banana pi

import serial		
import beanstalkc		
import json
import os

immx=0
immy=0
buffer=0
valstanga = 0

open_alprd = "/home/bananapi/openalpr/src/build/alprd --config /etc/openalpr"
os.system("pkill alprd")
os.system(open_alprd)

try:
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except:
	try:
		ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
	except:
		try:
			ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
		except:
			pass

beanstalk = beanstalkc.Connection(host='localhost', port=11300)
beanstalk.watch('alprd')

while True:

	f = open('/home/bananapi/Desktop/Database.conf','r')
	s=str(f.readlines())
	dati=eval(s)
		
	job = beanstalk.reserve()
	jobb = job.body
	job.delete()
	d = json.loads(jobb)

	time = str(d["processing_time_ms"])
	targa = str(d["results"][0]["plate"])
	x1 = str(d['results'][0]['coordinates'][0]['x'])
	y1 = str(d['results'][0]['coordinates'][0]['y'])
	x2 = str(d['results'][0]['coordinates'][1]['x'])
	y2 = str(d['results'][0]['coordinates'][1]['y'])
	x3 = str(d['results'][0]['coordinates'][2]['x'])
	y3 = str(d['results'][0]['coordinates'][2]['y'])
	x4 = str(d['results'][0]['coordinates'][3]['x'])
	y4 = str(d['results'][0]['coordinates'][3]['y'])
	immx = str(d['img_width'])
	immy = str(d['img_height'])	


	for num in range(0,40):		
		try:
			try:
				number_lines = len(dati)
				for i in range(0, number_lines):
					diz1 = eval(dati[i])
					targa_diz = diz1['targa']
					if (str(d['results'][0]['candidates'][num]['plate']) == targa_diz):
						try:
							ser.write("1")
						except:
							pass
						valstanga = 1
						nome = diz1['nome']			
						print "		Consento l'accesso!	", time," mS    ", nome
						

                                    
			except:
				pass                                      
                                
		except:
			pass

	
	
	trasm = dict()
	trasm["targa"]=nome
	trasm["tempo"]=time
	trasm["valstanga"]=valstanga
	trasm["x1"]=x1
	trasm["y1"]=y1
	trasm["x2"]=x2
	trasm["y2"]=y2
	trasm["x3"]=x3
	trasm["y3"]=y3
	trasm["x4"]=x4
	trasm["y4"]=y4
	trasm["immx"]=immx
	trasm["immy"]=immy
	
	f1 = open('/home/bananapi/Desktop/trasmissione.conf','w')
	f1.write (str(trasm))
