import requests
BASE_URL='http://127.0.0.1:8080/'
ENDPOINT='api/'

def get_resource():
    res=requests.get(BASE_URL+ENDPOINT)
    print(res.status_code)
    print(res.json())

# id=input("enter id")
get_resource()




