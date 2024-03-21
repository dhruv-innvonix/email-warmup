from rest_framework import serializers
from email_warmup.models import Timing

class TimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timing
        fields = '__all__'