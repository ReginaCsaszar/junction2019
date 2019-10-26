
'''
Tracking the train:
address: http://192.168.0.100:5000/rest/items
sensornumbering: 11,12,13, 21,22,23,24,25,26,27,31,32,33,34,35
values: default:1, train is detected:0

Control the trackswitch:
address: http://192.168.0.100:5000/rest/control/track_switch/x/y
2switches(s1,s2): ID:0,1, values: 0 – go straight, 1 – switch to the upper track

Lap time measuring:
http://192.168.0.100:5000/rest/track/statistics/lap_time

Train speed-motor control:
192.168.0.180/motor?params=xx:0-1023

Query gyroscope data: 192.168.0.180/gyro
you get the result on 192.168.0.180 (speed, accelarete, compass, temperature)

Buzzercontrol:
192.168.0.180/buzzer?params=x  x:desired frequency

Camera stream:
192.168.0.190:8080/stream

'''

import requests

x = requests.get('http://192.168.0.100:5000/rest/items')

print(x.text)
