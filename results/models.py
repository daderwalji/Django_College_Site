from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
    semester = models.CharField(max_length=20)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    registration_id = models.CharField(max_length=20)
    subject_1 = models.CharField(max_length=20,null=False)
    sub1 = models.IntegerField(default=0,blank=True,null=True)
    subject_2 = models.CharField(max_length=20,null=False)
    sub2 = models.IntegerField(default=0,blank=True,null=True)
    subject_3 = models.CharField(max_length=20,null=False)
    sub3 = models.IntegerField(default=0,blank=True,null=True)
    subject_4 = models.CharField(max_length=20,null=False)
    sub4 = models.IntegerField(default=0,blank=True,null=True)
    subject_5 = models.CharField(max_length=20,null=False)
    sub5 = models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.registration_id