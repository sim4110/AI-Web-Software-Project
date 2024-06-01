from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

from .models import Board

def list(request):
    board_list = Board.objects.all().order_by('-id')
    context = {
        'board_list':board_list,
    }
    return render(
        request,
        'board/list.html',
        context
    )

def list_walk(request):
    board_list = Board.objects.all().order_by('-id')
    context = {
        'board_list':board_list,
    }
    return render(
        request,
        'board/list_walk.html',
        context
    )

def list_wash(request):
    board_list = Board.objects.all().order_by('-id')
    context = {
        'board_list':board_list,
    }
    return render(
        request,
        'board/list_wash.html',
        context
    )

def list_grooming(request):
    board_list = Board.objects.all().order_by('-id')
    context = {
        'board_list':board_list,
    }
    return render(
        request,
        'board/list_grooming.html',
        context
    )

def read(request, id):
    board = Board.objects.get(pk=id)
    board.UpReadCount()
    return render(request, 'board/read.html', {'board':board})

def regist(request):
    if request.method == 'POST' :
        title = request.POST.get('title')
        type = request.POST.get('type')
        writer = request.POST.get('writer')
        content = request.POST.get('content')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        payment = request.POST.get('payment')
        zonecode = request.POST.get('zonecode')
        roadAddress = request.POST.get('roadAddress')
        roadAddressDetail = request.POST.get('roadAddressDetail')
        imgfile = request.FILES.get('imgfile')

        Board(title=title, type=type, writer=writer, content=content, startdate=startdate,
              enddate=enddate, payment=payment, zonecode=zonecode, 
              roadAddress=roadAddress, roadAddressDetail=roadAddressDetail, imgfile=imgfile).save()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/regist.html')

def edit(request, id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.type = request.POST.get('type')
        board.writer = request.POST.get('writer')
        board.content = request.POST.get('content')
        board.startdate = request.POST.get('startdate')
        board.enddate = request.POST.get('enddate')
        board.payment = request.POST.get('payment')
        board.zonecode = request.POST.get('zonecode')
        board.roadAddress = request.POST.get('roadAddress')
        board.roadAddressDetail = request.POST.get('roadAddressDetail')
        board.imgfile = request.FILES.get('imgfile')
        board.save()
        return redirect(reverse('board:read', args=(id,)))
    else:
        return render(request, 'board/edit.html', {'board':board})
    
def remove(request, id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.delete()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/remove.html', {'board':board})

def map(request,id):
    board = Board.objects.get(pk=id)
    return render(request, 'board/map.html', {'board':board})
    
