from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Weightage(models.Model):
    projects = models.IntegerField(null = True, default=50)
    workExperience = models.IntegerField(null = True, default=50)
    certifications = models.IntegerField(null = True, default=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.id

class CustomUser(AbstractUser):
    technicalSkills = models.CharField(max_length = 1000, null = True)
    educationalDetails = models.CharField(max_length = 1000, null = True)
    projects = models.CharField(max_length = 1000, null = True)
    workExperience = models.CharField(max_length = 1000, null = True)
    certifications = models.CharField(max_length = 1000, null = True)
    possiblePost = models.CharField(max_length = 500, null = True)
    recruiter = models.BooleanField(default=False)
    # weightage = models.ForeignKey(Weightage, null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.id



