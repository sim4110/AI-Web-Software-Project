from django.db import models
from django.utils import timezone
# Create your models here.


class StoreData(models.Model):
    writer = models.CharField(max_length=100, blank=True)
    writetime = models.CharField(max_length=100, default='00.00.00 00:00')
    store_name = models.CharField(max_length=100, blank=True)
    store_owner = models.CharField(max_length=100, blank=True)
    tel_num = models.CharField(max_length=15, blank=True)
    anesthesia = models.CharField(max_length=20, default='마취 없음')
    location = models.CharField(max_length=255, blank=True, null=True)
    opentime = models.TimeField(default='09:00')
    closetime = models.TimeField(default='18:00')
    store_image = models.ImageField(upload_to='store_images', blank=True, null=True)
    readcount= models.IntegerField(default=0)
    likecount=models.IntegerField(default=0)

    class Meta:
        db_table='store_data'

    def UpReadCount(self):
        self.readcount += 1
        self.save()

class Qualification(models.Model):
    pet_shop = models.ForeignKey(StoreData, related_name='qualifications', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255, blank=True)


class CommentData(models.Model):
    store = models.ForeignKey(StoreData, related_name='comments', on_delete=models.CASCADE)
    writer = models.CharField(max_length=100)
    content = models.TextField()
    writetime = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table='comment_data'


class LikeData(models.Model):
    store = models.ForeignKey(StoreData, related_name='likedata', on_delete=models.CASCADE)
    likeuser = models.CharField(max_length=100,blank=True)

    class Meta:
        db_table='store_like' 


   


    


