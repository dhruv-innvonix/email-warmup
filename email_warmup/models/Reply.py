from django.db import models

class Reply(models.Model):
    message = models.TextField()