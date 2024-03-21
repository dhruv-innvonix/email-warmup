from rest_framework import serializers
from email_warmup.models import EmailImprovement

class EmailImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailImprovement
        fields = '__all__'