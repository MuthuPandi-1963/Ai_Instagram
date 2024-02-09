from django.urls import path
from chat_bot.views import chat_bot_response

urlpatterns = [
    path('chat_bot/', chat_bot_response, name='chat_bot'),
]
