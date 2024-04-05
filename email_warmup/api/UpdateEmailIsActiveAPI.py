from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from email_warmup.models import EmailImprovement
from email_warmup.utility.encryption_util import encrypt, decrypt
@api_view(['PATCH'])
def UpdateEmailIsActiveAPI(request):
    if request.method == 'PATCH':
        email = request.data.get('email')
        is_active = request.data.get('is_active')

        # Check if email exists
        email_object = EmailImprovement.objects.filter(email=email).first()
        if email_object:
            email_object.is_active = is_active
            email_object.password = decrypt(email_object.password)
            email_object.app_pass_phrase = decrypt(email_object.app_pass_phrase)
            email_object.save()
            return Response({"message": "Email is_active status updated successfully", "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Email not found", "status": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
