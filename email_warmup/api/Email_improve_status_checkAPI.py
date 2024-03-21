from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from email_warmup.models import (
    EmailImprovement,
    GmailRecipient,
    OutlookRecipient,
    OtherRecipient
)

class Email_improve_status_checkAPI(APIView):
    def get(self, request, *args, **kwargs):
        filter_params = request.data
        if "email" in filter_params:
            import pdb; pdb.set_trace()
            try:
                FILTERING_QUERYSET = EmailImprovement.objects.get(
                    email=filter_params["email"])
                email_warmup_recipient = GmailRecipient.objects.all().count()
                email_warmup_recipient = OutlookRecipient.objects.all().count()
                email_warmup_recipient = OtherRecipient.objects.all().count()
                sp_number_mails_sent = FILTERING_QUERYSET.number_of_emails_sent
                warmup_email_count = FILTERING_QUERYSET.number_of_days_to_warmup
                email_improvement_check = email_warmup_recipient * warmup_email_count
                if ((email_improvement_check) <= (sp_number_mails_sent)):
                    return Response({"warmupcompleted": True,"status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
                else:
                    return Response({"warmupcompleted": False,"status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
            except:
                return Response({"error": f"email {filter_params['email']} not found", "status": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
