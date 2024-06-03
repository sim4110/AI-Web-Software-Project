from django.shortcuts import render,redirect
from .models import StoreData, Qualification, CommentData, LikeData, ScrapData

from django.contrib import messages
from django.utils import timezone

# Create your views here.


def store_regist(request) :
    try : 
        writer = request.session.get('user_id')
    except :
        writer = "unkown"   

    if request.method == 'POST':
        store_name = request.POST.get('STORE_NAME')
        store_owner = request.POST.get('STORE_OWNER')
        tel_num = request.POST.get('TEL_NUM')
        anesthesia = request.POST.get('anesthesia')
        opening_time = request.POST.get('OPENING_TIME')
        closing_time = request.POST.get('CLOSING_TIME')
        qualifications = request.POST.getlist('qualifications')
        store_image = request.FILES.get('STORE_IMAGE')

        postcode = request.POST.get('POSTCODE')
        address = request.POST.get('ADDRESS')
        detail_address = request.POST.get('DETAIL_ADDRESS')
        extra_address = request.POST.get('EXTRA_ADDRESS')

        writetime = timezone.now().strftime('%Y.%m.%d %H:%M')

        # 데이터베이스에 저장
        store_data = StoreData(
            writer=writer,
            writetime=writetime,
            store_name=store_name,
            store_owner=store_owner,
            tel_num=tel_num,
            anesthesia=anesthesia,
            opentime=opening_time,
            closetime=closing_time,
            
            postcode=postcode,
            address=address,
            detail_address=detail_address,
            extra_address=extra_address,
            store_image=store_image
        )

        if request.session.get('user_id') != None:
            store_data.save()
        else :
            return redirect('petgrooming:storeList')

        qualifications = request.POST.getlist('qualifications')
        for qualification in qualifications:
            if qualification:
                Qualification.objects.create(pet_shop=store_data, description=qualification)
        
        return redirect('petgrooming:storeList')

    else :
        return render(request, 'store/storeRegist.html', {'writer': writer})


def store_read(request,id) :
    # 데이터베이스에 저장된 특정 id값(userid아님 데이터 num id)글 데이터들 화면에 출력한다.
    # comment(댓글)작성, 수정, 삭제, 리스트 보여주기
    try:
        store = StoreData.objects.get(pk=id)
        comment_list = CommentData.objects.filter(store=store)
        user_id = request.session.get('user_id')

    except:
        store = None
        comment_list = None
        user_list = None
        user_id = 'unknown'

    if store != None:
        store.UpReadCount()

    #comment post 요청
    if request.method == 'POST':
        status = request.POST.get('STATUS')
        if status == 'CREATE':
            return comment_create(request, store)
        elif status == 'EDIT':    
            return comment_edit(request, store)
        elif status == 'DELETE':
            return comment_delete(request, store)
        elif status == 'LIKE' :
            if LikeData.objects.filter(store=store, likeuser=user_id).exists():
                messages.error(request, '이미 좋아요 버튼을 눌렀습니다.')
            else :
                if user_id is not None :
                    store.likecount += 1
                    user_list=LikeData(store = store, likeuser=user_id)
                    store.save()
                    user_list.save()
        return redirect('petgrooming:storeRead', id=id)
            
    else:
        return render(request,'store/storeRead.html', {'store':store, 'comments':comment_list})


def store_edit(request,id) :
    #데이터베이스에 저장된 특정 id값의 글 데이터들 <ipnut type>에 각각 띄워준다.
    #사용자가 <input type>의 내용을 수정한 값 받아온다.(method==post일 때) 
    #수정 버튼을 누르면 현재 로그인된 사용자가 특정 id값의 글의 작성자(writer)와 동일한지 확인한다.
    #만약 버튼을 누른 사용자가 글 작성자가 아닌경우 수정할 수 없다는 경고창을 띄우고 다시 화면을 보여준다.
    #만약 버튼을 누른 사용자가 글 작성자라면, 수정한 값을 불러온 데이터베이스 테이블의 특정 id 데이터에 업데이트한다.
    try:
        store = StoreData.objects.get(pk=id)
    except:
        store = None

    if request.method == 'POST':
        if store.writer == request.session.get('user_id'):
            store.store_name = request.POST.get('STORE_NAME')
            store.store_owner = request.POST.get('STORE_OWNER')
            store.tel_num = request.POST.get('TEL_NUM')
            store.anesthesia = request.POST.get('anesthesia')
            store.opentime = request.POST.get('OPENING_TIME')
            store.closetime = request.POST.get('CLOSING_TIME')
            
            store.postcode=request.POST.get('POSTCODE')
            store.address=request.POST.get('ADDRESS')
            store.detail_address=request.POST.get('DETAIL_ADDRESS')
            store.extra_address=request.POST.get('EXTRA_ADDRESS')      
            store.store_image = request.FILES.get('STORE_IMAGE')
            
            if store.opentime is None:
                store.opentime = '09:00'
            if store.closetime is None:
                store.closetime = '18:00'

            store.save()
            # messages.success(request, '홍보글을 업데이트했습니다.')
            return redirect('petgrooming:storeRead', id=id)
        
    else:
        # messages.error(request, '해당 홍보글 작성자가 아닙니다.')
        return render(request, 'store/storeEdit.html',{'store':store})


def store_delete(request, id) :
    #데이터베이스 저장된 특정 id값을 데이터를 삭제한다.
    if request.method == 'POST':
        try:
            store = StoreData.objects.get(pk=id)
            # comment_list = CommentData.objects.filter(store=store)
            # qualification_list = Qualification.objects.filter(store=store)

        except:
            store = None
        if store != None:
            if store.writer == request.session.get('user_id'):
                # comment_list.delete()
                # qualification_list.delete()
                store.delete()
                # messages.success(request, '홍보글 삭제를 완료했습니다.')
                return redirect('petgrooming:storeList')
            # else :
                # messages.error(request, '해당 홍보글 작성자가 아닙니다.')

            return redirect('petgrooming:storeRead', id=store.id)
        else :
            return redirect('petgrooming:storeList')


def store_list(request) :
    #작성해 등록한 글들 리스트 보여준다. 
    #등록된 각 글들 <a href>태그사용해 클릭하면 store read로 이어짐
    #++마이페이지, 좋아요 버튼 연동해야함
    store_list = StoreData.objects.all().order_by('-id')
    return render(request, 'store/storeList.html', {'stores': store_list})


#댓글기능
def comment_create(request, store) :
    if request.method == 'POST' :
        content = request.POST.get('content')
        new_comment = CommentData(
            store=store,
            writer=request.session.get('user_id'),
            content=content
        )
        new_comment.save()
    return redirect('petgrooming:storeRead', id=store.id)


def comment_delete(request,store) :
    if request.method == 'POST':
        comment_id  = request.POST.get('comment_id')
        comment = CommentData.objects.get(pk=comment_id)
        if comment.writer == request.session.get('user_id'):
            comment.delete()
        # else :
            # messages.error(request, '댓글 작성자가 아닙니다.')
    return redirect('petgrooming:storeRead', id=store.id)


def comment_edit(request, store) :
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        content = request.POST.get('content')
        comment = CommentData.objects.get(pk=comment_id)
        if comment.writer == request.session.get('user_id'):
            comment.content = content
            comment.save()
        # else:
            # messages.error(request, '댓글 작성자가 아닙니다.')
    return redirect('petgrooming:storeRead', id=store.id)


def comment_list(request) :
    store_list = StoreData.objects.all().order_by('-id')
    return render(request, 'store/storeList.html', {'stores': store_list})


def store_scrap(request,id) :
# 스크랩 등록 - 스크랩한 유저 id ScrapData 테이블에 저장
# 만약 스크랩 버튼 누른 유저가 이미 스크랩한 상태라면 스크랩 취소
# 아니면 스크랩에 유저 id 추가
    store = StoreData.objects.get(pk=id)
    user_id = request.session.get('user_id')
    
    if user_id is None:
        return redirect('main:login')

    if request.method == 'POST':
        if ScrapData.objects.filter(store=store, scrap_user=user_id).exists():
            #스크랩 취소 
            ScrapData.objects.filter(store=store, scrap_user=user_id).delete()
        else :
            #스크랩 추가
            ScrapData.objects.create(store=store, scrap_user=user_id)
            
    return redirect('petgrooming:storeRead',id=store.id)