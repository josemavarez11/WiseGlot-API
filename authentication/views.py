from datetime import timezone, datetime, timedelta
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.utils.crypto import get_random_string
from .models import ResetPassCode
from users.models import User
import jwt


# Create your views here.
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if(email is None or password is None):
        return Response({'error': 'Please provide both email and password'}, status=400)
    
    try:
        user = User.objects.get(ema_user=email, deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'The data provided does not match the data in the database.'}, status=400)
    
    if not check_password(password, user.pas_user):
        return Response({'error': 'The data provided does not match the data in the database.'}, status=400)
    
    token = jwt.encode({'user_id': str(user.id)}, 'SECRET_KEY', algorithm='HS256')

    user_data = {
        'id': user.id,
        'name': user.nam_user,
        'email': user.ema_user,
        'subscription': {
            'id': user.id_subscription_user.id,
            'description': user.id_subscription_user.des_subscription
        }
    }

    return Response({'user': user_data, 'token': token}, status=200)

@api_view(['POST'])
def send_reset_password_code(request):
    email = request.data.get('email')

    if email is None:
        return Response({'error': 'Please provide an email address'}, status=400)
    
    try:
        user = User.objects.get(ema_user=email, deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'No user associated with this email was found.'}, status=400)
    
    reset_pass_code = get_random_string(length=6, allowed_chars='0123456789acdefjhijklnopqrtuvwxyz')
    ResetPassCode.objects.create(id_user_reset_pass_code=user, val_reset_pass_code=reset_pass_code)

    html_message = render_to_string('email.html', {'code': reset_pass_code})
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject = 'Reset Password Code',
        body=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[email,]
    )

    message.attach_alternative(html_message, 'text/html')
    message.send()

    return Response({'message': 'Reset password code sent successfully'}, status=200)

    

@api_view(['POST'])
def validate_reset_password_code(request):
    code = request.data.get('code')
    email = request.data.get('email')

    if code is None or email is None:
        return Response({'error': "Please provide both secret code and email"}, status=400)

    try:
        reset_pass_code = ResetPassCode.objects.get(val_reset_pass_code=code, id_user_reset_pass_code__ema_user=email)
    except ResetPassCode.DoesNotExist:
        return Response({'error': 'The code provided is invalid.'}, status=400)
    
    date_to_compare = datetime.fromisoformat(str(reset_pass_code.created_at))
    current_time = datetime.now(timezone.utc)
    time_difference = current_time - date_to_compare
    
    if(time_difference > timedelta(minutes=5)):
        return Response({'error': 'The code provided has expired.'}, status=400)

    return Response({'message': 'Validation successfully completed.'}, status=200)

@api_view(['POST'])
def reset_password(request):
    code = request.data.get('code')
    password = request.data.get('password')
    email = request.data.get('email')

    if code is None or email is None or password is None:
        return Response({'error': 'Please provide all the required fields'}, status=400)
    
    try:
        ResetPassCode.objects.get(val_reset_pass_code=code)
    except ResetPassCode.DoesNotExist:
        return Response({'error': 'The code provided is invalid.'}, status=400)

    try:
        user = User.objects.get(ema_user=email, deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'No user associated with this email was found.'}, status=400)
    
    if check_password(password, user.pas_user):
        return Response({'error': 'The new password cannot be the same as the current password'}, status=400)
    
    user.pas_user = make_password(password)
    user.save()

    return Response({'message': 'Password successfully reset'}, status=200)