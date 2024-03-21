from email_warmup.SMTP_replying import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SMTP_ReplierAPI(APIView):
    def get(self, request):
        SMTP_reply_flow_starter_job()
        return Response({"message": "SMTP_Reply_Flow_Successfully_Executed!", "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)