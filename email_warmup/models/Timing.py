from django.db import models

class Timing(models.Model):
    mailing_time = models.TimeField()
    reply_time = models.TimeField()
