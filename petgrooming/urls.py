from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'petgrooming'

urlpatterns =[
    path('storelist/',views.store_list,name='storeList'),
    path('storeread/<int:id>',views.store_read,name='storeRead'),
    path('storeedit/<int:id>',views.store_edit,name='storeEdit'),
    path('storeremove/<int:id>', views.store_delete, name='storeDelete'),
    path('storeregist/', views.store_regist,name='storeRegist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)