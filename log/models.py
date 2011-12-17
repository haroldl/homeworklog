from django.db import models
from django.forms import ModelForm

class Log(models.Model):
    UNDERSTANDING_CHOICES = [
        (-1, "Not Answered"),
        ( 0, "Didn't Understand"),
        ( 1, "Understood a Little"),
        ( 2, "Mostly Understood"),
        ( 3, "Understood Completely")
    ]

    COMPLETION_CHOICES = [
        (0, "< 50%"),
        (1, "50-75%"),
        (2, "75-90%"),
        (3, "90-100%")
    ]

    first_name        = models.CharField(max_length=50)
    group             = models.CharField(max_length=50)
    assignment_title  = models.CharField(max_length=50)
    completion        = models.IntegerField(choices=COMPLETION_CHOICES)
    understanding     = models.IntegerField(choices=UNDERSTANDING_CHOICES)
    practice          = models.IntegerField(choices=UNDERSTANDING_CHOICES, blank=True, null=True)
    pushing           = models.IntegerField(choices=UNDERSTANDING_CHOICES, blank=True, null=True)
    pondering         = models.IntegerField(choices=UNDERSTANDING_CHOICES, blank=True, null=True)
    time              = models.CharField(max_length=50)
    help              = models.CharField(max_length=1000)
    collaboration     = models.CharField(max_length=1000)
    comments          = models.CharField(max_length=1000, blank=True)

class LogForm(ModelForm):
    class Meta:
        model = Log

class GroupInfo:
    group_ids = {
        '5 Air'   : '0',
        '5 Water' : '1',
        '6 Air'   : '2',
        '6 Water' : '3'
    }
