from django.urls import path
from .api import (
    EmailImprovementRegistrationAPI,
    Email_improve_status_checkAPI,
    SMTP_flowAPI,
    SMTP_ReplierAPI,
    UpdateEmailIsActiveAPI,
)
urlpatterns = [
    path('SenderEmail/', EmailImprovementRegistrationAPI, name='register'),
    path("WarmupStatus/", Email_improve_status_checkAPI.as_view()),
    path("SMTP_flow/", SMTP_flowAPI.as_view()),
    path("SMTP_reply_flow/", SMTP_ReplierAPI.as_view()),
    path("update-email-is-active/", UpdateEmailIsActiveAPI),
]
