from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from authentication.middlewares import jwt_required
from openai import OpenAI, OpenAIError, PermissionDeniedError
import os
from dotenv import load_dotenv
from .prompts import prompts
from .utils import build_user_presentation_msg
from .models import Message
from .serializers import MessageSerializer
from users.views import get_user_preferences_data
from users.models import User

load_dotenv()
# Create your views here.

@jwt_required
@api_view(['POST'])
def send_message(request):
    id_user = request.custom_user.id
    data = request.data.copy()
    if id_user is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        user = User.objects.get(pk=id_user)
        data['id_user'] = user.id
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        con_message = request.data.get('con_message')
        if con_message is None:
            return Response({'error': 'Please provide content for a message'}, status=400)

    create_msg_response(user.id, con_message)
    con_response = create_msg_response(user.id, con_message)
    data['con_response'] = con_response

    serializer = MessageSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({'con_message': con_response}, status=200)



def create_msg_response(user_id, content_message):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        raise ConnectionError("Failed to initialize OpenAI client") from e

    user_info = get_user_preferences_data(user_id)
    if user_info is None:
        raise ValueError(f"No preferences found for user ID {user_id}")

    try:
        user_presentation_msg = build_user_presentation_msg(user_info)
        print('Presentation message:', user_presentation_msg)
    except Exception as e:
        raise RuntimeError("Failed to build user presentation message") from e

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                { 
                    "role": "system",
                    "content": prompts['chat']['system']['english']
                },
                {"role": "user", "content": user_presentation_msg},
                {"role": "user", "content": content_message}
            ]
        )
    except PermissionDeniedError as e:
        raise RuntimeError("Country, region, or territory not supported") from e
    except OpenAIError as e:
        raise RuntimeError("OpenAI API request failed") from e
    except Exception as e:
        raise RuntimeError("An unexpected error occurred during the OpenAI API request") from e

    return response.choices[0].message.content
