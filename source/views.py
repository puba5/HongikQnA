from django.shortcuts import render

# Create your views here.

# 어플리케이션 생성 : 가상 환경이 실행되고 있는 상태에서 python manage.py startapp "어플리케이션 이름"
# 어플리케이션 등록 : 생성된 어플리케이션을 프로젝트 폴더의 settings.py에 등록해주어야된다
# static이나 template 폴더 생성 시 : static(혹은 template) 폴더 생성 후 폴더 하위에 어플리케이션과 같은 이름의 폴더 생성
# static 폴더와 파일 생성 후 : setting.py에 그 경로를 추가해 준 다음 python manage.py collectstatic 실행해주어야 함


def source(request):
    return render(request, 'source/source.html')