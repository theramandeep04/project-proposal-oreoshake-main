#from urllib import response

import matplotlib.pyplot as plt
import requests
import datetime  

while(True):
    
    uri_cnt = "http://127.0.0.1:8080/~/in-cse/in-name/WaterLevelData/WaterLevel?rcn=4"
    header = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }
    response = requests.get(uri_cnt, headers=header)
    data = response.json()
    data = data["m2m:cnt"]["m2m:cin"]

    x = []
    y = []

    c = 0
    for i in data:
        if c >= 1:
            x.append(int(c))
            y.append(float(i["con"]))
            pass
        c = c + 1
    plt.plot(x, y)
    plt.xlabel('ENTRY NAME')
    plt.ylabel('LIQUID LEVEL')
    plt.title('AUTOMATIC HAND SANITIZER LIQUID LEVEL')
    plt.show()
    plt.savefig('waterlevel.png')
    #average time to become empty
    #it's 5 hours by default
    x.append(int(0))
    y.append(int(5))
    uri_cnt = "http://127.0.0.1:8080/~/in-cse/in-name/UltrasonicSensor/HandDetection?rcn=4"
    header = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }
    response = requests.get(uri_cnt, headers=header)
    data = response.json()
    data = data["m2m:cnt"]["m2m:cin"]

    x = []
    y = []

    cnt={}
    c = 0
    for i in range(0,24):
        cnt[i]=0
    for i in data :
        date_time = datetime.datetime.fromtimestamp(str(i["con"]))
        hour=date_time.hour
        cnt[hour]=cnt[hour]+1
    for i in range(0,24):
        x.append(int(i))
        y.append(int(hour))
    plt.plot(x, y)
    plt.xlabel('ENTRY NAME')
    plt.ylabel('LIQUID LEVEL')
    plt.title('AUTOMATIC HAND SANITIZER LIQUID LEVEL')
    plt.show()
    uri_cnt = "http://127.0.0.1:8080/~/in-cse/in-name/WaterLevelData/WaterLevel?rcn=4"
    plt.savefig('handData.png')

    # print(response.text)
    # print(type(response))

