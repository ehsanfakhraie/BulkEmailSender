from django.contrib import admin
from bulk_email.models import Receiver


# Register your models here.
@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    pass
