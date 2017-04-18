from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=211)
    email = models.CharField(max_length=211)
    password = models.CharField(max_length=211)

#returns name + email as string
    def __str__(self):
        return self.name + ' . ' + self.email

#Creating database columns for User.

class Profile(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=1024)
    profile_pic = models.CharField(max_length=211)

# returns info as string
    def __str__(self):
        return self.info

#SCreating User profile like info and profile picture.

class Post(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=2500)
    post_pic = models.CharField(max_length=211)
    post_date = models.DateField((u"Blog Date"), blank=True)
    post_time = models.TimeField((u"Blog Time"), blank=True)

#Creates blogpost with time and date


