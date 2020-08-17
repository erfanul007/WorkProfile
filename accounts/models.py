from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length = 32, null=True)
    First_name = models.CharField(max_length = 32, null=True)
    Last_name = models.CharField(max_length = 32, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' sensitive'


class UserContact(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    email = models.CharField(max_length = 32, null=True)
    phone = models.CharField(max_length = 32, null=True)
    Nationality = models.CharField(max_length = 32, null=True)
    CurrentAddress = models.CharField(max_length = 124, null=True)
    PermanentAddress = models.CharField(max_length = 124, null=True)
    ZipCode = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' contact'

class UserDetails(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    marital_status = models.CharField(max_length = 32, null=True)
    gender = models.CharField(max_length = 32, null=True)
    religion = models.CharField(max_length = 32, null=True)
    blood_group = models.CharField(max_length = 32, null=True)
    age = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' details'


class UserSkills(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    topic = models.CharField(max_length = 32, null=True)
    details = models.CharField(max_length = 124, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' skills'


class UserExperiences(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    WorkTitle = models.CharField(max_length = 32, null=True)
    CompanyName = models.CharField(max_length = 124, null=True)
    details = models.CharField(max_length = 124, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' experience'

class UserProjects(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    ProjectTitle = models.CharField(max_length = 32, null=True)
    usededenv = models.CharField(max_length = 124, null=True)
    details = models.CharField(max_length = 124, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' project'

class UserAchievements(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    prize = models.CharField(max_length = 32, null=True)
    field = models.CharField(max_length = 32, null=True)
    details = models.CharField(max_length = 124, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' achieve'

class UserGoal(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    goal = models.CharField(max_length = 32, null=True)
    details = models.CharField(max_length = 124, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' goal'


class UserPassion(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    passion = models.CharField(max_length = 32, null=True)
    details = models.CharField(max_length = 124, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' passion'



class UserSchool(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    school = models.CharField(max_length = 124, null=True)
    passing_year = models.IntegerField(null=True)
    GPA = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' school'


class UserCollege(models.Model):
    GROUP = (
        ('Sience','Sience'),
        ('Commerce','Commerce'),
        ('Arts', 'Arts'),
            )
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    college = models.CharField(max_length = 124, null=True)
    group = models.CharField(max_length = 32, null=True, choices=GROUP)
    passing_year = models.IntegerField(null=True)
    GPA = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' college'


class UserUniversity(models.Model):
    DEGREE = (
        ('B.Sc','B.Sc'),
        ('B.Com','B.Com'),
        ('B.A','B.A'),
        ('M.Sc','M.Sc'),
        ('M.Com','M.Com'),
        ('M.A','M.A'),
        ('PhD', 'PhD'),
        ('Diploma','Diploma')
            )
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    varsity = models.CharField(max_length = 124, null=True)
    degree = models.CharField(max_length = 32, null=True, choices=DEGREE)
    feild = models.CharField(max_length = 32, null=True)
    passing_year = models.IntegerField(null=True)
    CGPA = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username + ' varsity'
