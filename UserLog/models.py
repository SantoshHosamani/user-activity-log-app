from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

class ActivityPeriods(models.Model):
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()

class User(models.Model):
    
    user_id = models.TextField()
    real_name = models.TextField()
    tz = models.TextField()
    activity_periods = ListField(EmbeddedModelField('ActivityPeriods'))