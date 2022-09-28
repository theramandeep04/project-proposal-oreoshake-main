import time
import requests
import smtplib, ssl 
epoch_time = int(time.time())-300

while(True) :
    cur_time = int(time.time())
    if cur_time - epoch_time >= 300 :
        epoch_time=cur_time
        uri_cnt = "http://127.0.0.1:8080/~/in-cse/in-name/WaterLevelData_/WaterLevel_/la"
        header = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/json'
        }
        response = requests.get(uri_cnt, headers=header)
        data = response.json()
        data=data["m2m:cin"]["con"]
        print(int(data))
        if int(data)>1:
            continue
       
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email = "zaidcoder@gmail.com"
        receiver_email = "pranjali.bishnoi@gmail.com"
        password = "uplrlgegoxcblxqn"
        message = "ALERT! SANITIZER LEVEL IS LOW"
            # Create a secure SSL context
        context = ssl.create_default_context()
            # Try to log in to server and send email

        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        print(server.sendmail(sender_email, receiver_email, message))