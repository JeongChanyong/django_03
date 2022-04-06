from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    comment = models.TextField() # 자기 소개
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="user/%y/%m") # 폴더별 관리 > media / user / 년 / 월 

    

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/no.jpg"