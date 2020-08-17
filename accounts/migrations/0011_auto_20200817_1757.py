# Generated by Django 3.1 on 2020-08-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200817_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercollege',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usercontact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userexperiences',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usergoal',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userpassion',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprojects',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userschool',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userskills',
            name='user',
        ),
        migrations.RemoveField(
            model_name='useruniversity',
            name='user',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='CompanyName',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='CurrentAddress',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='Nationality',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='PermanentAddress',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ProjectTitle',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ZipCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='achcieveprize',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='achieveetails',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='achievefield',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='blood_group',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='collegeGPA',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='collegeName',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='college_passing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='collegegroup',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='goaldetails',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='goaltopic',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='marital_status',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='passiondetails',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='passiontopic',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='previousWorkTitle',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='previousWorkdetails',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='projectdetails',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='projectusededenv',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='religion',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='schoolGPA',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='schoolName',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='school_passing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='skilldetails',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='skillname',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='varistydegree',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='varsity_CGPA',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='varsity_passing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='varsityfeild',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='varsityname',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.DeleteModel(
            name='UserAchievements',
        ),
        migrations.DeleteModel(
            name='UserCollege',
        ),
        migrations.DeleteModel(
            name='UserContact',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
        migrations.DeleteModel(
            name='UserExperiences',
        ),
        migrations.DeleteModel(
            name='UserGoal',
        ),
        migrations.DeleteModel(
            name='UserPassion',
        ),
        migrations.DeleteModel(
            name='UserProjects',
        ),
        migrations.DeleteModel(
            name='UserSchool',
        ),
        migrations.DeleteModel(
            name='UserSkills',
        ),
        migrations.DeleteModel(
            name='UserUniversity',
        ),
    ]
