from django.db import models
# Create your models here.

class UserData(models.Model):
    userid = models.CharField(max_length=20, verbose_name='ID')
    password = models.CharField(max_length=20, verbose_name='PW')
    usernickname = models.CharField(max_length=20, verbose_name='NICKNAME')
    phonenumber = models.CharField(max_length=11,verbose_name='TEL')
    email = models.EmailField(max_length=100, verbose_name='EMAIL')
    
    class Meta:
        db_table = 'userData'