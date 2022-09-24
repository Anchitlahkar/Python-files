import requests

for i in range(1,100):
    URL = f"http://ec2-3-6-91-214.ap-south-1.compute.amazonaws.com/profile?id={i}"
    r = requests.get(url=URL)

    if r.status_code == 200:
        print(URL)

