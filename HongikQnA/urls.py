"""HongikQnA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

# main 어플리케이션의 views파일을 import 해야한다
import main.views
import source.views
import account.views

urlpatterns = [
    # path 함수 인자 설명
    # 1번째 인자 의 주소가 들어오면
    # 2번째 인자의 함수를 실행한다

    path('admin/', admin.site.urls),

    path('', main.views.start, name='start'),
    path('write/', main.views.write, name='write'),
    path('write/submit/', main.views.submit, name='submit'),

    path('source/', source.views.source, name='source'),
    
    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),
]
