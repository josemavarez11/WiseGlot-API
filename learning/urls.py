from django.urls import path
from . import views
from authentication.middlewares import JWTMiddleware, AdminMiddleware

urlpatterns = [
    path('create-language/', views.create_language, name='create-language'), #OK
    path('delete-language/<uuid:pk>/', views.delete_language, name='delete-language'), #OK
    path('update-language/<uuid:pk>/', views.update_language, name='update-language'), #OK
    path('get-languages/', views.get_languages, name='get-languages'), #OK
    path('create-language-level/', views.create_language_level, name='create-language-level'), #OK
    path('delete-language-level/<uuid:pk>/', views.delete_language_level, name='delete-language-level'), #OK
    path('update-language-level/<uuid:pk>/', views.update_language_level, name='update-language-level'), #OK
    path('get-language-levels/', views.get_language_levels, name='get-language-levels'), #OK
    path('create-reason-to-study/', views.create_reason_to_study, name='create-reason-to-study'), #OK
    path('delete-reason-to-study/<uuid:pk>/', views.delete_reason_to_study, name='delete-reason-to-study'), #OK
    path('update-reason-to-study/<uuid:pk>/', views.update_reason_to_study, name='update-reason-to-study'), #OK
    path('get-reasons-to-study/', views.get_reasons_to_study, name='get-reasons-to-study'), #OK
    path('create-topic/', views.create_topic, name='create-topic'), #OK
    path('delete-topic/<uuid:pk>/', views.delete_topic, name='delete-topic'), #OK
    path('update-topic/<uuid:pk>/', views.update_topic, name='update-topic'), #OK
    path('get-topics/', views.get_topics, name='get-topics'), #OK
    path('create-user-preference/', JWTMiddleware(views.create_user_preference), name='create-user-preference'), #user
    path('delete-user-preference/<uuid:pk>/', AdminMiddleware(views.delete_user_preference), name='delete-user-preference'), #just admin
    path('update-user-preference/<uuid:pk>/', AdminMiddleware(views.update_user_preference), name='update-user-preference'), #just admin
    path('get-user-preferences/', AdminMiddleware(views.get_user_preferences), name='get-user-preferences'), #just admin
    path('create-user-preference-topic/', JWTMiddleware(views.create_user_preference_topic), name='create-user-preference-topic'), #user
    path('delete-user-preference-topic/<uuid:pk>/', AdminMiddleware(views.delete_user_preference_topic), name='delete-user-preference-topic'), #just admin
    path('update-user-preference-topic/<uuid:pk>/', AdminMiddleware(views.update_user_preference_topic), name='update-user-preference-topic'), #just admin
    path('get-user-preference-topics/', AdminMiddleware(views.get_user_preference_topics), name='get-user-preference-topics'), #user
]
