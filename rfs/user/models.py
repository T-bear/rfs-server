from django.db import models

# Create your models here.

class User():
    name = models.CharField(211)
    email = models.CharField(211)
    password = models.CharField(211)

#Creating database columns for User.

class Profile():
    info = models.CharField(1024)
    profile_pic = models.CharField(211)
    #FK ?

#SCreating User profile like info and profile picture.

class Post():
    post = models.CharField(2500)
    post_pic = models.CharField(211)
    post_date = models.DateField((u"Blog Date"), blank=True)
    post_time = models.TimeField((u"Blog Time"), blank=True)

#Creates blogpost with time and date


