from django.db import models

class Log(models.Model):
    first_name        = models.CharField(max_length=50)
    assignment_title  = models.CharField(max_length=50)
