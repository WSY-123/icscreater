from django.urls import re_path, path, include
from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', views.login, name='login'),
    path('process/', views.process, name='process'),
]