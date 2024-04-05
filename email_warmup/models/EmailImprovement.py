from django.db import models
from email_warmup.utility.encryption_util import encrypt, decrypt

# Create your models here.

class EmailImprovement(models.Model):
    name = models.CharField(max_length=80,null=False,blank=False)
    email = models.EmailField(max_length=150, default="")
    password = models.CharField(max_length=200, default="")
    smtp_port = models.CharField(max_length=15, default="")
    smtp_host = models.CharField(max_length=50, default="")
    is_active = models.BooleanField(default=False)
    number_of_days_to_warmup = models.IntegerField(default=60)
    app_pass_phrase = models.CharField(max_length=200, default="",null=True,blank=True)
    number_of_emails_sent = models.IntegerField(default=0)
    email_type=models.CharField(max_length=80,null=False,blank=False)
    
    def save(self, *args, **kwargs):
        self.password = encrypt(self.password)
        self.app_pass_phrase = encrypt(self.app_pass_phrase)
        super(EmailImprovement, self).save(*args, **kwargs)