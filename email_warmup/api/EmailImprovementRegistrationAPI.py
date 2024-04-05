from rest_framework.response import Response
from rest_framework import status
from email_warmup.serializers import (
    EmailImprovementSerializer,
)
from rest_framework.decorators import api_view
from email_warmup.models import EmailImprovement

@api_view(['POST'])
def EmailImprovementRegistrationAPI(request):
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        # Check if email already exists
        existing_email = EmailImprovement.objects.filter(email=email).first()
        if existing_email:
            email_is_active = existing_email.is_active
            return Response({"error": "Email already registered", "email_is_active": email_is_active}, status=status.HTTP_400_BAD_REQUEST)
        
        password = request.data.get('password')
        smtp_port = request.data.get('smtp_port')
        smtp_host = request.data.get('smtp_host')
        is_active = request.data.get('is_active')
        number_of_days_to_warmup = request.data.get('number_of_days_to_warmup')
        app_pass_phrase = request.data.get('app_pass_phrase')
        number_of_emails_sent = request.data.get('number_of_emails_sent')
        email_type = request.data.get('email_type')
        data = {"name": name, "email": email,
                "password": password, "smtp_port": smtp_port, "smtp_host": smtp_host, "is_active": is_active, "number_of_days_to_warmup": number_of_days_to_warmup, "app_pass_phrase": app_pass_phrase,
                "number_of_emails_sent": number_of_emails_sent, "email_type": email_type}
        serializer = EmailImprovementSerializer(data=data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_200_OK}, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
