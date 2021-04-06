from django.shortcuts import render, redirect
from furl import furl
from django.http import HttpResponseRedirect,HttpResponse
import requests
import json
import os

# Create your views here.
def login(request):
    return render(request,'user/login.html',locals())

def process(request):
    f = furl(request.get_full_path())
    code = f.args['code']
    url = 'https://jaccount.sjtu.edu.cn/oauth2/token'
    client_id = '1ps1konnBmIKL7Wi3ZtF'
    client_secret = '6197CD7F37979ED0F24F0E57F8C7F4CE3EB30B7C1061EC32'
    grant_type = 'authorization_code'
    redirect_uri = 'http://127.0.0.1:8000/user/process/'
    data = {
        'grant_type': grant_type,
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }
    result = requests.post(url, data)
    strResult = json.loads(result.text)
    id_token = strResult['id_token']
    access_token = strResult['access_token']
    headers = {"Authorization": "Bearer {}".format(access_token)}
    url = 'https://api.sjtu.edu.cn/v1/me/lessons/2018-2019-1?access_token=' + access_token
    r = requests.request(url=url, method='GET', headers=headers, timeout=(20, 60))
    entities = json.loads(r.text).get('entities')
    # print(entities)
    # for entity in entities:
    #     print(entity)
    dic = entities[0]
    dic0 = dic['teachers'][0]
    # print(dic0['name'])

    print(type(entities))
    FILE_PATH = 'D:\PyProjects\icscreater\DATA'
    with open('{}\lessonsdata.json'.format(FILE_PATH), 'w', encoding='UTF-8') as fp:
        fp.write(json.dumps(entities,ensure_ascii=False,indent=2))
        fp.close()
    # 运行文件处理程序
    os.system("python jsonprocess.py")

    return redirect('http://127.0.0.1:8000/settime/form')
