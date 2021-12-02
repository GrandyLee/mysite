from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
from myapp.models import Event


def index(request):
    # return HttpResponse("Hello,World!")
    return render(request, "index.html")


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # if username == 'admin' and password == 'admin123':
            request.session['user'] = username  # 将session信息记录到浏览器
            respone = HttpResponseRedirect('/event_manage/')
            # respone.set_cookie('user', username, 3600)  #  添加浏览器cookie
            return respone
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器的session
    return render(request, "event_manage.html", {"user": username, "events": event_list})
