from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.middlewares import admin_required, jwt_required
from .serializers import LanguageSerializer, LanguageLevelSerializer, ReasonToStudySerializer, TopicSerializer, UserPreferenceSerializer, UserPreferenceTopicSerializer
from .models import Language, LanguageLevel, ReasonToStudy, Topic, UserPreference, UserPreferenceTopic
from users.models import User

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

@jwt_required
@api_view(['POST'])
def create_user_preference(request):
    user_id = request.custom_user.id
    if user_id is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    if request.method == 'POST':
        data = request.data.copy()
        data['id_user'] = user_id
        serializer = UserPreferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['PUT'])
def update_user_preference(request, pk):
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

@admin_required 
@api_view(['DELETE'])
def delete_user_preference(request, pk):
    try:
        user_preference = UserPreference.objects.get(pk=pk)
    except UserPreference.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user_preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@jwt_required
@api_view(['GET'])
def get_user_preference(request):
    user_id = request.custom_user.id
    if user_id is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        user_preferences = UserPreference.objects.filter(id_user=user_id)
    except UserPreference.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserPreferenceSerializer(user_preferences, many=True)

    user = User.objects.get(pk=user_id)
    native_language = Language.objects.get(pk=serializer.data[0]['id_native_language'])
    language_to_study = Language.objects.get(pk=serializer.data[0]['id_language_to_study'])
    language_to_study_level = LanguageLevel.objects.get(pk=serializer.data[0]['id_language_to_study_level'])
    reason_to_study = ReasonToStudy.objects.get(pk=serializer.data[0]['id_reason_to_study'])
    user_preferece_topic = UserPreferenceTopic.objects.filter(id_user_preference=serializer.data[0]['id'])
    topics = []
    for topic in user_preferece_topic:
        topics.append({
            "id_topic": topic.id_topic_id,
            "description": Topic.objects.get(pk=topic.id_topic_id).des_topic
        })
    
    response_data = {
        "id_user_preference": serializer.data[0]['id'],
        "user": {
            "id_user": user.id,
            "name": user.nam_user,
            "email": user.ema_user
        },
        "native_language": {
            "id_native_language": native_language.id,
            "description": native_language.des_language
        },
        "language_to_study": {
            "id_language_to_study": language_to_study.id,
            "description": language_to_study.des_language
        },
        "language_to_study_level": {
            "id_language_to_study_level": language_to_study_level.id,
            "description": language_to_study_level.des_language_level
        },
        "reason_to_study": {
            "id_reason_to_study": reason_to_study.id,
            "description": reason_to_study.des_reason_to_study
        },
        "topics": topics
    }

    return Response(response_data, status=status.HTTP_200_OK)
   
#---------------------------------------------------

#------------------- USER PREFERENCE TOPIC CRUD ----

@jwt_required
@api_view(['POST'])
def create_user_preference_topic(request):
    if request.method == 'POST':
        serializer = UserPreferenceTopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@admin_required
@api_view(['PUT'])
def update_user_preference_topic(request, pk):
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

@admin_required
@api_view(['DELETE'])
def delete_user_preference_topic(request, pk):
    try:
        user_preference_topic = UserPreferenceTopic.objects.get(pk=pk)
    except UserPreferenceTopic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user_preference_topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@jwt_required
@api_view(['GET'])
def get_user_preference_topics(request):
    user_id = request.custom_user.id
    if user_id is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        user_preference = UserPreference.objects.get(id_user=user_id)
        user_preference_topics = UserPreferenceTopic.objects.filter(id_user_preference=user_preference.id)
    except UserPreferenceTopic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    topics = []

    for user_preference_topic in user_preference_topics:
        topic = Topic.objects.get(pk=user_preference_topic.id_topic_id)
        topics.append({
            "id_topic": topic.id,
            "description": topic.des_topic
        })

    response_data = {
        "id_user": user_id,
        "id_user_preference": user_preference.id,
        "topics": topics
    }

    return Response(response_data, status=status.HTTP_200_OK)
    
#---------------------------------------------------