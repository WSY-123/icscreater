from django.http import HttpResponse
from django.shortcuts import render,redirect

# 时间原点设置表单
def settime_form(request):
    return render(request, 'settime.html')
# 提醒功能配置表单
def setalarm_form(request):
    return render(request, 'setalarm.html')

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