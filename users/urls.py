from django.urls import path
from . import views
from authentication.middlewares import JWTMiddleware

urlpatterns = [
    path('create-profile/', views.create_profile, name='create-profile'), #OK
    path('delete-profile/<uuid:pk>/', views.delete_profile, name='delete-profile'), #OK
    path('create-subscription/', views.create_subscription, name='create-subscription'), #OK
    path('delete-subscription/<uuid:pk>/', views.delete_subscription, name='delete-subscription'), #OK
    path('create-user/', views.create_user, name='create-user'), #OK
    path('delete-user/<uuid:pk>/', JWTMiddleware(views.delete_user), name='delete-user'), #user
    path('update-user/<uuid:pk>/', JWTMiddleware(views.update_user), name='update-user'), #user
    path('get-user-data/<uuid:pk>/', JWTMiddleware(views.get_user_data), name='get-user-data'), #user
]