import time
import requests
import os
import datetime

while True:
    
    POST_URL = os.environ['POST_URL']
    POST_SECONDS = os.environ['POST_SECONDS']
    
    with open("/app/temp", "rb") as f:
        temp = f.read()
        f.close()
        
    with open("/app/hostname", "rb") as f:
        hostname = f.read()
        f.close()
        
    json_data = { 'temp': temp, 'hostname': hostname }
    
    x = requests.post(POST_URL, json = json_data)
    print(datetime.datetime.now().isoformat,': ',x)
    print(datetime.datetime.now().isoformat,': ','POSTd ', json_data, ' to ',POST_URL)
    print(datetime.datetime.now().isoformat,': ','Sleeping for ', POST_SECONDS,' seconds...')
    time.sleep(POST_SECONDS)