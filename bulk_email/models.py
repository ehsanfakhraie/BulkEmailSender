from django.db import models


# Create your models here.
class Receiver(models.Model):
    email = models.EmailField()
    name = models.TextField()
    publication = models.TextField()
    email_sent = models.ForeignKey('email_service.EmailLog', on_delete=models.DO_NOTHING, blank=True, null=True)
