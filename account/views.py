from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# redirect : url을 다시 바꾸기 위해 import
# User : django에서 기본적으로 제공하는 user 모델이다
# auth : User을 쓰기 위해서 갖고와야하는 놈

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # 해당 username이 존재하는지 확인한 후 그렇지 않은 경우에 User를 생성한다 
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'account/signup.html', {'error': 'Username already been taken'})
            except:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('start')
        else:
            return render(request, 'account/signup.html', {'error': 'Password must match'})
    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        # user가 존재하는 경우 로그인, 그렇지 않을 경우 에러 메세지 출력
        if user is not None:
            auth.login(request, user)
            return redirect('start')
        else:
            return render(request, 'account/login.html', {'error': 'Username or Password is incorrect'})
    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('start')
    return render(request, 'account/signup.html')