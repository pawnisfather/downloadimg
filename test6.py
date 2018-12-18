import requests
import json

def a():
    github_url = "http://apitest.ely.work/api/user/user/login"
    datas = json.dumps({'account': 'caogu', 'password': 'caogu'})
    date2= {'account': 'caogu', 'password': 'caogu'}
    print(datas)
    data2 = {'account': 'caogu', 'password': "caogu"}
    data3 = {"data":{"account":"caogu", "password":"caogu"}}
    r = requests.post(url=github_url, data=data2)
    # requests.post(url, data=json.dumps(params), headers={'Content-Type': 'application/json'})

    print(r.json())
    s= json.loads(r.text)
    print(s.keys())
    print(s['data']['id'])



if __name__ == '__main__':
    a()

