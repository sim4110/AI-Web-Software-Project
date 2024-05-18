from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserData
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup/signup.html')

    elif request.method == 'POST':    
        userid=request.POST.get('ID_SIGNUP')
        password=request.POST.get('PW_SIGNUP')
        repassword=request.POST.get('PW_CHECK_SIGNUP')
        usernickname=request.POST.get('NICKNAME_SIGNUP')
        email=request.POST.get('EMAIL_SIGNUP')
        phonenumber=request.POST.get('TEL_NUM_SIGNUP')

        res_data={}

        if(password == repassword):
            user = UserData(
                userid=userid,
                password=password,
                usernickname=usernickname,
                email=email,
                phonenumber=phonenumber
            )
            user.save()
            return redirect('main:login')

        else :
            res_data=['password Wrong']
            return HttpResponse(res_data)

def user_login(request):
    if request.method == 'GET':
        return render(request,'login/login.html')

    elif request.method == 'POST' :
        userid=request.POST.get('ID_LOGIN')
        userpw=request.POST.get('PW_LOGIN')
        
        try:
            users = UserData.objects.get(userid=userid)
        except:
            users=None

        if users is not None:
            if users.password == userpw:
                request.session['user_id']=userid
                request.session['user_nickname']=users.usernickname
                return redirect('main:home')                
            else :
                messages.info(request, "비밀번호를 다시 입력해 주세요.")
                return redirect('main:login')
        else :
            messages.info(request,"ID를 다시 입력해 주세요." )
            return redirect('main:login')

def user_logout(request):
    del request.session['user_id']
    del request.session['user_nickname']
    return redirect('main:login')

def main(request):
    return render(request,'main/main.html')




