# Generated by Django 5.0.6 on 2024-05-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_board_roadaddress_board_roadaddressdetail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='roadAddress',
            field=models.CharField(default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='roadAddressDetail',
            field=models.CharField(default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='zonecode',
            field=models.CharField(default=0, max_length=30, null=True),
        ),
    ]
