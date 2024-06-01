# Generated by Django 3.2.25 on 2024-05-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petgrooming', '0003_alter_postdata_writer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='postData',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='profileImg',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='roadAddress',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='roadAddressDetail',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='species',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='storename',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='storeowner',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='telnumber',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='zonecode',
        ),
        migrations.AddField(
            model_name='storedata',
            name='anesthesia',
            field=models.CharField(default='마취 없음', max_length=20),
        ),
        migrations.AddField(
            model_name='storedata',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='storedata',
            name='qualifications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='storedata',
            name='store_image',
            field=models.ImageField(blank=True, null=True, upload_to='store_images/'),
        ),
        migrations.AddField(
            model_name='storedata',
            name='store_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='storedata',
            name='store_owner',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='storedata',
            name='tel_num',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='storedata',
            name='writer',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='storedata',
            name='writetime',
            field=models.CharField(default='00.00.00 00:00', max_length=100),
        ),
        migrations.AlterField(
            model_name='storedata',
            name='closetime',
            field=models.TimeField(default='18:00'),
        ),
        migrations.AlterField(
            model_name='storedata',
            name='opentime',
            field=models.TimeField(default='09:00'),
        ),
    ]