from django.shortcuts import render
from .models import Post
# Create your views here.

def start(request):
    posts = Post.objects
    return render(request, 'main/start.html', {'posts':posts})

    # main 어플리케이션 아래에는 templates/main/ 위치 아래에 html 파일이,  static/main/ 위치 아래에 css 파일이 있다
    # view에서 html파일, 그리고 html에서 css파일로 연결이 된다