from django.shortcuts import render, HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
from chatterbot.trainers import ListTrainer
from .models import Conversation

with open('data.json') as file:
    data = json.load(file)

patterns = []
responses = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
    for response in intent['responses']:
        responses.append(response)

bot = ChatBot('chatbot', read_only=False)
trainer = ListTrainer(bot)
trainer.train(patterns)
trainer.train(responses)


def main(request):
    return render(request, 'main.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage', None)
    chatResponse = str(bot.get_response(userMessage))
    Conversation.objects.create(user_input=userMessage, bot_response=chatResponse)
    return HttpResponse(chatResponse)
    