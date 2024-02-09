from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chat_bot.models import ChatMessage
from django.shortcuts import render 
@csrf_exempt
def chat_bot_response(request):
    if request.method == 'POST':
        data = request.POST
        user_message = data.get('message')
        
        # Here you can implement your logic to handle different settings-related queries
        # For now, let's just provide a simple response
        
        response_message = "To turn on dark mode, go to your Instagram settings and look for the 'Dark Mode' option."
        
        # Save the chat message to the database
        ChatMessage.objects.create(user="User", message=user_message)
        
        return render(request, 'chat_bot.html', {'message': response_message})
    else:
        return JsonResponse({'error': 'Invalid request method'})
