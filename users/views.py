from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from authentication.middlewares import admin_required, jwt_required
from .models import Profile, Subscription, User
from learning.models import UserPreference, UserPreferenceTopic, LanguageLevel, Language, ReasonToStudy, Topic
from .serializers import ProfileSerializer, SubscriptionSerializer, UserSerializer
import jwt

# Create your views here.

#------------------- PROFILE CRUD -------------------

@admin_required
@api_view(['POST'])
def create_profile(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['DELETE'])
def delete_profile(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#---------------------------------------------------

#------------------- SUBSCRIPTION CRUD --------------

@admin_required
@api_view(['POSt'])
def create_subscription(request):
    if request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['DELETE'])
def delete_subscription(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------

#------------------- USER CRUD ----------------------

@jwt_required
@api_view(['GET'])
def get_user_data(request):
    user_id = request.custom_user.id
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def get_user_preferences_data(user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user_preferences = UserPreference.objects.filter(id_user=user_id).select_related(
        'id_native_language', 'id_language_to_study', 'id_language_to_study_level', 'id_reason_to_study'
    )

    if not user_preferences.exists():
        return None

    preferences_data = []

    for preference in user_preferences:
        preference_topics = UserPreferenceTopic.objects.filter(id_user_preference=preference.id).select_related('id_topic')
        topics_data = [topic.id_topic.des_topic for topic in preference_topics]

        preferences_data.append({
            'native_language': preference.id_native_language.des_language,
            'language_to_study': preference.id_language_to_study.des_language,
            'language_to_study_level': preference.id_language_to_study_level.des_language_level,
            'reason_to_study': preference.id_reason_to_study.des_reason_to_study,
            'topics': topics_data
        })

    user_info = {
        "name": user.nam_user,
        "preferences": preferences_data
    }
    
    return user_info


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        ema_user = request.data.get('ema_user')
        if User.objects.filter(ema_user=ema_user).exists():
            return Response({'message': 'Email already exists'}, status=status.HTTP_409_CONFLICT)
        
        data = request.data.copy()
        data['pas_user'] = make_password(data['pas_user'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            token = jwt.encode({'user_id': str(serializer.data['id'])}, 'SECRET_KEY', algorithm='HS256')
            return Response({'user': serializer.data, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@jwt_required    
@api_view(['DELETE'])
def delete_user(request):
    user_id = request.custom_user.id
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.deleted = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

@jwt_required 
@api_view(['PUT'])
def update_user(request):
    try:
        user = User.objects.get(pk=request.custom_user.id)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if(request.data == {}):
            return Response({'message': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data.copy()

        if 'pas_user' in data:
            if not check_password(data['pas_user'], user.pas_user):
                data['pas_user'] = make_password(data['pas_user'])
            else:
                data.pop('pas_user')

        updated_data = {key: value for key, value in data.items() if getattr(user, key) != value}

        if not updated_data:
            return Response({'message': 'The data provided matches with the current data.'}, status=status.HTTP_304_NOT_MODIFIED)
        
        serializer = UserSerializer(user, data=updated_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---------------------------------------------------