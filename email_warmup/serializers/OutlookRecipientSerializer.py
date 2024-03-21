from rest_framework import serializers
from email_warmup.models import OutlookRecipient

class OutlookRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutlookRecipient
        fields = '__all__'