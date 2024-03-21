from django.db import models

class Message(models.Model):
    message = models.TextField()