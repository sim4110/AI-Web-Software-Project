from django.urls import path
from . import views

app_name = 'main'

urlpatterns =[
    path('signup/', views.signup, name='signup'),
    path('home/', views.main, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout,name='logout'),
]