from django.contrib import admin

from django.contrib import admin
from chatbotapp.models import Conversation

class ConversationAdmin(admin.ModelAdmin):
    list_display = ["user_input", "bot_response", "created_date"]


admin.site.register(Conversation, ConversationAdmin)