import time
import requests
import os
import datetime

while True:
    
    POST_URL = os.environ['POST_URL']
    POST_SECONDS = int(os.environ['POST_SECONDS'])
    
    with open("/app/temp", "rb") as f:
        temp = int(f.read())
        f.close()
        
    with open("/app/hostname", "rb") as f:
        hostname = f.read().decode().strip()
        f.close()
        
    json_data = { 'temp': temp, 'host': hostname }
    print(datetime.datetime.now().isoformat(),': ','POSTing ', json_data, ' to ',POST_URL,' ...')
    x = requests.post(POST_URL, json = json_data)
    print(datetime.datetime.now().isoformat(),': ',x)
    print(datetime.datetime.now().isoformat(),': ','Sleeping for ', POST_SECONDS,' seconds...')
    
    time.sleep(POST_SECONDS)