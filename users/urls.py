"""为应用程序users定义URL模式"""

# from django.conf.urls import url
from django.contrib.auth.views import LoginView
# from django.contrib.auth import login
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    # 登录页面
    # re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    re_path(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    # re_path(r'^login/$', views.login, name="login"),

    # 注销
    re_path(r'^logout/$', views.logout_view, name='logout'),

    # 注册页面
    re_path(r'^register/$', views.register, name='register'),
]

app_name = 'users'