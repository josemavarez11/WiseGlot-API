from django.urls import path
from . import views

urlpatterns = [
    path('send-message/', views.send_message, name='send-message'),
    path('get-messages-by-user/', views.get_messages_by_user, name='get-messages-by-user')
]