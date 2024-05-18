from django.db import models
import uuid

# Create your models here.
class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    des_subscription = models.CharField(max_length=90)
    pri_subscription = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'subscription'

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    des_profile = models.CharField(max_length=100)

    class Meta:
        db_table = 'profile'

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_subscription_user = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    id_profile_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nam_user = models.CharField(max_length=300)
    ema_user = models.CharField(max_length=300)
    pas_user = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'