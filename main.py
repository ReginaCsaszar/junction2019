
'''
Tracking the train:
address: http://192.168.0.100:5000/rest/items
sensornumbering: 11,12,13, 21,22,23,24,25,26,27,31,32,33,34,35
values: default:1, train is detected:0

response:
{
"track":
    {
    "rail_sections":
        {
        "11":{"pin":17,"state":1},
        "12":{"pin":27,"state":1},
        "13":{"pin":22,"state":0},
        "21":{"pin":10,"state":1},
        "22":{"pin":9,"state":1},
        "23":{"pin":11,"state":1},
        "24":{"pin":5,"state":1},
        "25":{"pin":6,"state":1},
        "26":{"pin":13,"state":1},
        "27":{"pin":19,"state":1},
        "31":{"pin":26,"state":1},
        "32":{"pin":21,"state":1},
        "33":{"pin":20,"state":1},
        "34":{"pin":16,"state":1},
        "35":{"pin":12,"state":1}
        },
    "rail_switches":
        {
        "1":null,
        "2":null
        },
    "statistics":
        {
        "lap_time":
            {
            "12_35_10":6.222411870956421,
            "12_35_16":5.016779184341431,
            "12_43_22":315.8744659423828,
            "12_53_04":579.5206949710846,
            "12_56_16":190.19687509536743,
            "13_00_13":235.51980805397034,
            "13_01_47":93.3273561000824,
            "13_02_37":49.31740689277649,
            "13_03_00":22.87215495109558,
            "13_07_33":271.4660210609436,
            "13_14_31":417.05844497680664,
            }
        }
    }
}

Control the trackswitch:
address: http://192.168.0.100:5000/rest/control/track_switch/x/y
2switches(s1,s2): ID:0,1, values: 0 – go straight, 1 – switch to the upper track

Lap time measuring:
http://192.168.0.100:5000/rest/track/statistics/lap_time

Train speed-motor control:
192.168.0.180/motor?params=xx:0-1023

Query gyroscope data: 192.168.0.180/gyro
you get the result on 192.168.0.180 (speed, accelarete, compass, temperature)

response:
{
'variables': 
    {
    'speed': 0, 
    'lights': 1, 
    'direction': 1, 
    'Ax': -0.69, 
    'Ay': 0.59, 
    'Az': -0.11, 
    'T': 28.01, 
    'Gx': -2.77, 
    'Gy': -1.4, 
    'Gz': -0.22}, 
    'id': '1', 
    'name': 'Nokia Garage Lab', 
    'hardware': 'esp8266', 
    'connected': True
    }
}

Buzzercontrol:
192.168.0.180/buzzer?params=x  x:desired frequency

Camera stream:
192.168.0.190:8080/stream

'''

import requests

x = requests.get('http://192.168.0.100:5000/rest/items')

print(x.text)
