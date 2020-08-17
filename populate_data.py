import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WorkProfile.settings')

import django
django.setup()

import random
from accounts.models import UserInfo, UserSchool, UserCollege, UserUniversity
from faker import faker

FakeGen = Faker()

def add_user():
    fake_user = FakeGen.username()
    fake_fname = FakeGen.first_name()
    fake_lname = FakeGen.last_name()
    fake_email = FakeGen.email()
    fake_phone = FakeGen.phone_number()
    user = UserInfo.objects.get_or_create(username=fake_user, First_name=fake_fname, Last_name=fake_lname, email=fake_email, phone = fake_phone)

    user.save()

    return user
    

def populate(N=5):
    for entry in range(N):
        user = add_user()
