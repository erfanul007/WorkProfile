# Generated by Django 3.1 on 2020-08-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_userinfo_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='workFeild',
            field=models.CharField(max_length=124, null=True),
        ),
    ]
