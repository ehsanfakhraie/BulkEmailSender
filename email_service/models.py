from django.db import models


# Create your models here.

class EmailLog(models.Model):
    to = models.EmailField()
    date_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    subject = models.CharField(max_length=2000)
    body_html = models.TextField()
    body_text = models.TextField()
