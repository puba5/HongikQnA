from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
# Create your views here.

# main 어플리케이션 아래에는 templates/main/ 위치 아래에 html 파일이,  static/main/ 위치 아래에 css 파일이 있다
# view에서 html파일, 그리고 html에서 css파일로 연결이 된다

def start(request):
    posts = Post.objects
    return render(request, 'main/start.html', {'posts':posts})

def write(request):
    return render(request, 'main/write.html')

# 데이터베이스에 동적으로 받은 모델의 정보를 저장하는 코드
def submit(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.save()
    return redirect('/')