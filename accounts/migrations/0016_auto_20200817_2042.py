# Generated by Django 3.1 on 2020-08-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200817_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='collegeBoard',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='schoolBoard',
            field=models.CharField(max_length=124, null=True),
        ),
    ]
