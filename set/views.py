from django.http import HttpResponse
from django.shortcuts import render,redirect
#
# 表单
def settime_form(request):
    return render(request, 'settime.html')

def setalarm_form(request):
    return render(request, 'setalarm.html')
#
# # 接收请求数据
# def search(request):
#     request.encoding='utf-8'
#     if 'q' in request.GET and request.GET['q']:
#         message = '你搜索的内容为: ' + request.GET['q']
#     else:
#         message = '你提交了空表单'
#     return HttpResponse(message)

def settime(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        with open('D:\\PyProjects\icscreater\DATA\\timeinput.txt','w')as f:
            f.write(request.GET['q'])
        return redirect('http://127.0.0.1:8000/settime/alarm_form')

def setalarm(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        with open('D:\\PyProjects\icscreater\DATA\\alarminput.txt','w')as f:
            f.write(request.GET['q'])
        return HttpResponse('内容配置成功，已将文件保存到本地目录下，感谢使用！')