from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.middlewares import admin_required
from .serializers import LanguageSerializer, LanguageLevelSerializer, ReasonToStudySerializer, TopicSerializer, UserPreferenceSerializer, UserPreferenceTopicSerializer
from .models import Language, LanguageLevel, ReasonToStudy, Topic, UserPreference, UserPreferenceTopic

# Create your views here.

#------------------- TOPICS CRUD -------------------

@admin_required
@api_view(['POST'])
def create_topic(request):
    if request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['PUT'])
def update_topic(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data.copy()

        updated_data = {key: value for key, value in data.items() if value is not None}

        if not updated_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TopicSerializer(topic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['DELETE'])
def delete_topic(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def get_topics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

#---------------------------------------------------

#------------------- LANGUAGE CRUD -----------------

@admin_required
@api_view(['POST'])
def create_language(request):
    if request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required 
@api_view(['PUT'])
def update_language(request, pk):
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data.copy()

        updated_data = {key: value for key, value in data.items() if value is not None}

        if not updated_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = LanguageSerializer(language, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['DELETE'])
def delete_language(request, pk):
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_languages(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)
   
#---------------------------------------------------

#------------------- LANGUAGE LEVEL CRUD -----------

@admin_required
@api_view(['POST'])
def create_language_level(request):
    if request.method == 'POST':
        serializer = LanguageLevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['PUT'])
def update_language_level(request, pk):
    try:
        language_level = LanguageLevel.objects.get(pk=pk)
    except LanguageLevel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data.copy()

        updated_data = {key: value for key, value in data.items() if value is not None}

        if not updated_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = LanguageLevelSerializer(language_level, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['DELETE'])
def delete_language_level(request, pk):
    try:
        language_level = LanguageLevel.objects.get(pk=pk)
    except LanguageLevel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        language_level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_language_levels(request):
    language_levels = LanguageLevel.objects.all()
    serializer = LanguageLevelSerializer(language_levels, many=True)
    return Response(serializer.data)
     
#---------------------------------------------------

#------------------- REASON TO STUDY CRUD ----------

@admin_required
@api_view(['POST'])
def create_reason_to_study(request):
    if request.method == 'POST':
        serializer = ReasonToStudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['PUT'])
def update_reason_to_study(request, pk):
    try:
        reason_to_study = ReasonToStudy.objects.get(pk=pk)
    except ReasonToStudy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data.copy()

        updated_data = {key: value for key, value in data.items() if value is not None}

        if not updated_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ReasonToStudySerializer(reason_to_study, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['DELETE'])
def delete_reason_to_study(request, pk):
    try:
        reason_to_study = ReasonToStudy.objects.get(pk=pk)
    except ReasonToStudy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        reason_to_study.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_reasons_to_study(request):
    reasons_to_study = ReasonToStudy.objects.all()
    serializer = ReasonToStudySerializer(reasons_to_study, many=True)
    return Response(serializer.data)
   
#---------------------------------------------------

#------------------- USER PREFERENCE CRUD ----------

@api_view(['POST'])
def create_user_preference(request):
    #this endpoint must be protected by a middleware that checks if the user is an Admin 
    if request.method == 'POST':
        serializer = UserPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user_preference(request, pk):
    #this endpoint must be protected by a middleware that checks if the user is an Admin 
    try:
        user_preference = UserPreference.objects.get(pk=pk)
    except UserPreference.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data.copy()

        updated_data = {key: value for key, value in data.items() if value is not None}

        if not updated_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserPreferenceSerializer(user_preference, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user_preference(request, pk):
    #this endpoint must be protected by a middleware that checks if the user is an Admin 
    try:
        user_preference = UserPreference.objects.get(pk=pk)
    except UserPreference.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user_preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_user_preferences(request):
    user_preferences = UserPreference.objects.all()
    serializer = UserPreferenceSerializer(user_preferences, many=True)
    return Response(serializer.data)
   
#---------------------------------------------------

#------------------- USER PREFERENCE TOPIC CRUD ----

@api_view(['POST'])
def create_user_preference_topic(request):
    #this endpoint must be protected by a middleware that checks if the user is an Admin 
    if request.method == 'POST':
        serializer = UserPreferenceTopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user_preference_topic(request, pk):
    #this endpoint must be protected by a middleware that checks if the user is an Admin 
    try:
        user_preference_topic = UserPreferenceTopic.objects.get(pk=pk)
    except UserPreferenceTopic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data.copy()

        updated_data = {key: value for key, value in data.items() if value is not None}

        if not updated_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserPreferenceTopicSerializer(user_preference_topic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user_preference_topic(request, pk):
    #this endpoint must be protected by a middleware that checks if the user is an Admin 
    try:
        user_preference_topic = UserPreferenceTopic.objects.get(pk=pk)
    except UserPreferenceTopic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user_preference_topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_user_preference_topics(request):
    user_preference_topics = UserPreferenceTopic.objects.all()
    serializer = UserPreferenceTopicSerializer(user_preference_topics, many=True)
    return Response(serializer.data)
    
#---------------------------------------------------