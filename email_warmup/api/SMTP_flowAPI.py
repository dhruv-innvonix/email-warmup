from email_warmup.SMTP_mailing import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SMTP_flowAPI(APIView):
    def get(self, request):
        SMTP_mailing_job()
        return Response({"message": "SMTP_flow_Executed!", "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
