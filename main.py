import requests

for i in range(5000):
    
    url1=f"http://ec2-3-6-91-214.ap-south-1.compute.amazonaws.com/order?id=2"
    r = requests.get(url=url1)
    print(r.status_code)
    if(r.status_code==200):
        print(url1)
    