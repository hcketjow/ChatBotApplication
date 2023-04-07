from django.db import models
from django.utils import timezone

class Conversation(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_input
    
