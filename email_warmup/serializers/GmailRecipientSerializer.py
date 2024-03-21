from rest_framework import serializers
from email_warmup.models import GmailRecipient

class GmailRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmailRecipient
        fields = '__all__'