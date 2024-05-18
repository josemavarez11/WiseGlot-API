from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), #OK
    path('send-reset-password-code/', views.send_reset_password_code, name='send_reset_password_code'), #OK
    path('validate-reset-password-code/', views.validate_reset_password_code, name='validate_reset_password_code'), #OK
    path('reset-password/', views.reset_password, name='reset_password'), #OK
]