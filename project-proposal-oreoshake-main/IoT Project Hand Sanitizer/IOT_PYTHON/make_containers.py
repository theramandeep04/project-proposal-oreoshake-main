from declare_functions import *
uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
ae  = "WaterLevelData_"
cnt = "WaterLevel_"
create_ae(uri_cse, ae)
uri_ae = uri_cse + "/" + ae
create_cnt(uri_ae, cnt)
ae  = "WaterLevelData_"
cnt = "Epoch_"
uri_ae  = uri_cse + "/" + ae
uri_cnt = uri_ae + "/" + cnt
create_cnt(uri_ae,cnt)
ae = "UltrasonicSensor_"
cnt = "HandDetection_"
uri_ae = uri_cse + "/" + ae
uri_cnt = uri_ae + "/" + cnt
create_ae(uri_cse, ae)
create_cnt(uri_ae, cnt)