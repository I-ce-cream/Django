"""one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


"""
导入url编写模块
from django.urls import path,include

导入admin功能模块
from django.contrib import admin

整个项目的url集合  每个元素代表一条url信息
urlpatterns
"""
from django.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # 设置admin的url
    # 第一个参数  url地址 即  http://127.0.0.1:8000/admin/   admin后面的斜杠为路径的分隔符
    # admin.site.urls   是url对应的视图函数
    path('admin/', admin.site.urls),


    # 如果url为空  代表网站域名  127.0.0.1:8000 通常为网站首页  include 是将应用中的urls包含进来
    path('', include('myapp.urls'))
    # 另一种写法
    # 直接使用from将app导入进来
    # from myapp import urls as app_urls
    # path('',inclde(app_urls))

    # 扩展  网址分两部分
    # domain      url
    # 127.0.0.1   admin
]
