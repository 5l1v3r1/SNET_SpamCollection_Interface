from django.db import models

class chatData(models.Model):
    group_name = models.TextField()
    username = models.CharField(max_length=100)
    text_content = models.TextField()
    is_spam = models.BooleanField(default=False)