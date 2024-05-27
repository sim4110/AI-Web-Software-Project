from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('list_walk/', views.list_walk, name='list_walk'),
    path('list_wash/', views.list_wash, name='list_wash'),
    path('list_grooming/', views.list_grooming, name='list_grooming'),
    path('read/<int:id>/', views.read, name='read'),
    path('regist/', views.regist, name='regist'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('remove/<int:id>/', views.remove, name='remove'),
    path('map/<int:id>/', views.map, name='map'),
]
