from django.contrib import admin

# Register your models here.
from email_service.models import EmailLog


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    pass
