from datetime import datetime
f = open('location.txt', 'a')

import paho.mqtt.client as mqtt

now=datetime.now()
f.write( +", "+now.strftime("%b%d %H:%M:%S")+'\n') 