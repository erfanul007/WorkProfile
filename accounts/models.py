from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length = 32, null=True)

    profile_pic = models.ImageField(null=True, blank=True)

    First_name = models.CharField(max_length = 32, null=True,blank=True)
    Last_name = models.CharField(max_length = 32, null=True, blank=True)
    email = models.CharField(max_length = 32, null=True, blank=True)
    phone = models.CharField(max_length = 32, null=True, blank=True)
    Nationality = models.CharField(max_length = 32, null=True, blank=True)
    CurrentAddress = models.CharField(max_length = 124, null=True, blank=True)
    PermanentAddress = models.CharField(max_length = 124, null=True, blank=True)
    workFeild = models.CharField(max_length = 124, null=True, blank=True)
    ZipCode = models.IntegerField(null=True, blank=True)

    marital_status = models.CharField(max_length = 32, null=True, blank=True)
    gender = models.CharField(max_length = 32, null=True, blank=True)
    religion = models.CharField(max_length = 32, null=True, blank=True)
    blood_group = models.CharField(max_length = 32, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    schoolName = models.CharField(max_length = 124, null=True, blank=True)
    school_passing_year = models.IntegerField(null=True, blank=True)
    schoolBoard = models.CharField(max_length = 124, null=True, blank=True)
    schoolGPA = models.FloatField(null=True, blank=True)

    collegeName = models.CharField(max_length = 124, null=True, blank=True)
    collegegroup = models.CharField(max_length = 32, null=True, blank=True)
    college_passing_year = models.IntegerField(null=True, blank=True)
    collegeBoard = models.CharField(max_length = 124, null=True, blank=True)
    collegeGPA = models.FloatField(null=True, blank=True)

    varsityname = models.CharField(max_length = 124, null=True, blank=True)
    varistydegree = models.CharField(max_length = 32, null=True, blank=True)
    varsityfeild = models.CharField(max_length = 32, null=True, blank=True)
    varsity_passing_year = models.IntegerField(null=True, blank=True)
    varsity_CGPA = models.FloatField(null=True, blank=True)

    skillname = models.CharField(max_length = 32, null=True, blank=True)
    skilldetails = models.CharField(max_length = 124, null=True, blank=True)

    previousWorkTitle = models.CharField(max_length = 32, null=True, blank=True)
    CompanyName = models.CharField(max_length = 124, null=True, blank=True)
    previousWorkdetails = models.CharField(max_length = 124, null=True, blank=True)

    ProjectTitle = models.CharField(max_length = 32, null=True, blank=True)
    projectusededenv = models.CharField(max_length = 124, null=True, blank=True)
    projectdetails = models.CharField(max_length = 124, null=True, blank=True)

    achcieveprize = models.CharField(max_length = 32, null=True, blank=True)
    achievefield = models.CharField(max_length = 32, null=True, blank=True)
    achieveetails = models.CharField(max_length = 124, null=True, blank=True)

    goaltopic = models.CharField(max_length = 32, null=True, blank=True)
    goaldetails = models.CharField(max_length = 124, null=True, blank=True)

    passiontopic = models.CharField(max_length = 32, null=True, blank=True)
    passiondetails = models.CharField(max_length = 124, null=True, blank=True)

    aboutme = models.CharField(max_length = 124, null=True, blank=True)



    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
