from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.http import HttpResponse
from .models import UserData
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(userid=userid, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/home')
                else :
                    messages.error(request, "login fail")

        else :
            res_data=['password Wrong']
            return HttpResponse(res_data)

def user_login(request):
    if request.method == 'GET':
        return render(request,'login/login.html')

    elif request.method == 'POST' :
        userid=request.POST.get('ID_LOGIN')
        userpw=request.POST.get('PW_LOGIN')

        user = authenticate(request, userid=userid,password=userpw)
        if user is not None:
            login(request, user)
            return redirect('/home')

        else :
            messages.info(request, "ID/비밀번호를 다시 입력해 주세요.")
            return redirect('main:login')
            

def main(request):
    return render(request,'main/main.html')




