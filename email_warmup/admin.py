# Register your models here.
from django.contrib import admin
from .models import (
    EmailImprovement,
    GmailRecipient,
    OutlookRecipient,
    OtherRecipient,
    Reply,
    Subject,
    Message,
    Timing,
)


admin.site.register(EmailImprovement)


MAX_OBJECTS = 5
MAX_RECIPIENT_MAILS = 100


@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['subject']
    # other class attributes can be set here as well.

    # To allow the user to be able to add only 5 objects/rows for this model (The Post Model).
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


@admin.register(Message)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['message']
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


@admin.register(Reply)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['message']
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


@admin.register(Timing)
class TimingAdmin(admin.ModelAdmin):
    list_display = ['mailing_time', 'reply_time']
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]


class GmailRecipientAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(GmailRecipient)
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_RECIPIENT_MAILS:
            return False
        return super().has_add_permission(request)


class OutlookRecipientAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(OutlookRecipient)
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_RECIPIENT_MAILS:
            return False
        return super().has_add_permission(request)


class OtherRecipientAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(OtherRecipient)
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_RECIPIENT_MAILS:
            return False
        return super().has_add_permission(request)


admin.site.register(OutlookRecipient, OutlookRecipientAdmin)
admin.site.register(OtherRecipient, OtherRecipientAdmin)
admin.site.register(GmailRecipient, GmailRecipientAdmin)



