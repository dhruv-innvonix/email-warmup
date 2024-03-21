from rest_framework import serializers
from email_warmup.models import OtherRecipient

class OtherRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherRecipient
        fields = '__all__'