from django.db import models

from django.utils import timezone
#from django.contib.auth.models import User
class Home(models.Model):
     mar1=models.CharField(max_length=200)

class About(models.Model):
    text = models.TextField(max_length= 5000)

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.TextField()
    date=models.DateTimeField(default=timezone.now)

class Meeting(models.Model):
    no = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=32)
    summary = models.TextField()
    agenda = models.TextField(default="")
    date =models.DateTimeField(default=timezone.now)

class Member(models.Model):
    name = models.CharField(max_length=32)
    post =models.CharField(max_length=32)
    image =models.ImageField(upload_to='prof_image')
    phn_number = models.CharField(max_length=12)
    email = models.EmailField()
    info =models.TextField(max_length=200)
    address =models.CharField(max_length=400)

    def get_email(self):
        return str(self.email)

    def get_no(self):
        m=len(self.email)
        return m

class Account(models.Model):
    no= models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    task = models.CharField(max_length=50)
    amount = models.CharField(max_length=100)
    total=models.CharField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    subject=models.CharField(max_length=50,default='',blank=True)
    comment=models.TextField(max_length=500)
    date = models.DateTimeField(default=timezone.now)


class Images(models.Model):
    title=models.CharField(max_length=100)
    description =models.CharField(max_length=50)
    image=models.ImageField(upload_to='static/media')

class Send_Email(models.Model):
    subject=models.CharField(max_length=50,default='',blank=True)
    message = models.TextField(max_length=500)
    date =  models.DateTimeField(default=timezone.now)

    def get_message(self):
        return str(self.message)

    def get_subject(self):
        return str(self.subject)