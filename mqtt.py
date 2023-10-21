from datetime import datetime
f = open('location.txt', 'a')

#reading from mqtt
import paho.mqtt.client as mqtt


#writing
now=datetime.now()
f.write( +", "+now.strftime("%b%d %H:%M:%S")+'\n') 