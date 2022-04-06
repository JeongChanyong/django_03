from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import User
# from os import rename


def update(request):
    if request.method == "POST":
        u = request.user
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        if up:
            u.set_password(up)
        u.comment = uc
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        login(request, u)
        return redirect("acc:profile")       
    return render(request, 'acc/update.html')


def delete(request):
    u = request.user
    ck = request.POST.get("pwck")
    if check_password(ck, u.password):
        u.pic.delete() 
        u.delete()
        return redirect("acc:index")     
    else:
        pass
        return redirect("acc:profile")


def profile(requset):
    context = {
        
    }
    return render (requset, 'acc/profile.html', context)


def signup(request):
    if request.method == "POST":        
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        up1 = request.POST.get("upass1")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic") # user 사진 전송
        # print(un, up, uc, pi)
        if up==up1:
            try:            
                User.objects.create_user(username=un, password=up,
                comment=uc, pic=pi)
                return redirect("acc:index")
            except:
                messages.info(request, '동일한 계정이 있습니다. 다시 작성해주세요')
        else:
            messages.warning(request, '비밀번호가 틀렸어요. 다시 작성해주세요')
    return render(request, 'acc/signup.html')


def logout_user(request):
    logout(request)
    return redirect('acc:login')


def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)      # 계정 인증
        if u:                                           
            login(request, u)
            messages.success(request, f"Welcome {u}")   # 계정 인증이 되었다면 user의 정보를 request에 담아준다
            return redirect('acc:index')
        else:
            messages.error(request, "계정 정보가 일치 하지 않습니다.") 

    return render(request, 'acc/login.html')

def index(request):
    return render(request, "acc/index.html")




