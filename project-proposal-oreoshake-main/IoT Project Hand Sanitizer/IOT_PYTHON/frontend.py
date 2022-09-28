from multiprocessing import connection
import flask
from flask import Flask, request, render_template
from flask import request
import requests
import time
import datetime
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    uri_cnt = "http://127.0.0.1:8080/~/in-cse/in-name/WaterLevelData_/WaterLevel_?rcn=4"
    header = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }
    response = requests.get(uri_cnt, headers=header)
    data = response.json()
    data = data["m2m:cnt"]["m2m:cin"]
    data_level = data
    x = []
    y = []
    idx = -1
    for i in data:
        if(float(i["con"])>7):
            continue
        y.append(float(i["con"]))
    uri_cnt = "http://127.0.0.1:8080/~/in-cse/in-name/WaterLevelData_/Epoch_?rcn=4"
    header = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }
    response = requests.get(uri_cnt, headers=header)
    data = response.json()
    data = data["m2m:cnt"]["m2m:cin"]
    epoch_data = data
    idx = -1
    for i in data:
        idx = idx + 1
        if(float(data_level[idx]["con"])>7):
            continue
        cur=float(i["con"])
        x.append(cur)

    uri_cnt = "http://127.0.0.1:8080/~/in-cse/in-name/UltrasonicSensor_/HandDetection_?rcn=4"
    header = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }
    response = requests.get(uri_cnt, headers=header)
    data = response.json()
    data = data["m2m:cnt"]["m2m:cin"]
    xx = []
    yy = []
    cnt = {}
    for i in range(0,24):
        cnt[i]=0
    for i in data:
        epoch = i['con']
        hour=time.localtime(int(epoch)).tm_hour
        print(hour)
        cnt[int(hour)] = cnt[int(hour)] + 1
    for i in range(0,24):
        xx.append(i)
        yy.append(cnt[i])

    idx=0          #index of the list
    st_time=-1     #start_time=-1
    xxx=[]         #x-axis
    yyy=[]         #y-axis
    thres_min=2    #minimum threshold
    thres_max=5    #maximum threshold
    for cur in data_level:
        cur_time =  float(epoch_data[idx]["con"])
        cur_level = float(cur["con"])
        if cur_level >= 1000:
            continue
        if(cur_level>=thres_max):
            st_time=cur_time
        if(cur_level<=thres_min and st_time!=-1):
            xxx.append(cur_time)
            yyy.append(((int(cur_time)-int(st_time))))
            st_time=-1
        idx = idx + 1
    return render_template('index.html',x=x,y=y,xx=xx,yy=yy,xxx=xxx,yyy=yyy)
app.run()