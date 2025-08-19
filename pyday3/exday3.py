
'''response = requests.get(
f"{BASE}/user-agent",
timeout=5
)
response.raise_for_status()
status = response.status_code
conttent = response.headers["content-type"]
data = response.json()

print("Status code:", status)
print("Content-Type:", conttent)
print("Response JSON:", data)
print("user-agent:", data["user-agent"])
'''
'''
import os, time 
import requests
BASE = "http://httpbin.org"


response1 = requests.post(
f"{BASE}/response-headers",
params = {'freeform' : 'test'},
timeout=5
)
response1.raise_for_status
content = response1.headers['content-type']
data = response1.json()
print(data)
'''

'''
payload = {"email": "student@example.com", "subscribe":True}
response1 = requests.post(
f"{BASE}/anything",
json= payload,
timeout=5
)
response1.raise_for_status
content = response1.headers['content-type']
data = response1.json()
'''
import os, time 
import requests
BASE = "http://httpbin.org"
with requests.session() as s:
   # s.headers.update({"user-agent","day2"})
    for i in range(3):
        r=s.get(f"{BASE}/user-agent", timeout=5)
        x=s.get(f"{BASE}/ip")
        if r.status_code == 200 and x.status_code == 200:
            break
    print(r.status_code)
    print(r.json())
    print(x.json())