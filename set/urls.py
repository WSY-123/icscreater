from django.urls import re_path, path, include
from django.conf.urls import url
from . import views

app_name = 'set'
urlpatterns = [
    # 信息输入表单及提交后的反馈页面
    path('', views.settime, name='settime'),
    path('form/',views.settime_form, name='settime_form'),
    path('alarm_form/',views.setalarm_form,name='setalarm_form'),
    path('setalarm/',views.setalarm,name='setalarm')
]