from django.db import models


class TemporaryRecipient(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    password = models.CharField(max_length=200, default="")
    app_pass_phrase = models.CharField(max_length=200, default="")
    imap_port = models.CharField(max_length=15, default="")
    smtp_port = models.CharField(max_length=15, default="")
    smtp_host = models.CharField(max_length=50, default="")
    imap_host = models.CharField(max_length=50, default="")
    email_type = models.CharField(max_length=50, default="")
    today_email_sent = models.BooleanField()

    def __str__(self):
        return self.name
