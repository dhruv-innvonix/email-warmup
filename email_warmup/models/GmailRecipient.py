from django.db import models
from email_warmup.utility.encryption_util import encrypt

class GmailRecipient(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    password = models.CharField(max_length=200, default="")
    app_pass_phrase = models.CharField(max_length=200, default="")
    imap_port = models.CharField(max_length=15, default="")
    smtp_port = models.CharField(max_length=15, default="")
    smtp_host = models.CharField(max_length=50, default="")
    imap_host = models.CharField(max_length=50, default="")

    def save(self, *args, **kwargs):
        self.password = encrypt(self.password)
        self.app_pass_phrase=encrypt(self.app_pass_phrase)
        super(GmailRecipient, self).save(*args, **kwargs)