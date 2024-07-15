from django.db import models
import uuid

# Create your models here.
class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    abb_language = models.CharField(max_length=10, unique=True, null=True)
    des_language = models.CharField(max_length=90)

    class Meta:
        db_table = 'language'

class LanguageLevel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    des_language_level = models.CharField(max_length=90)

    class Meta:
        db_table = 'language_level'

class ReasonToStudy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    des_reason_to_study = models.CharField(max_length=150)

    class Meta:
        db_table = 'reason_to_study'

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    des_topic = models.CharField(max_length=150)

    class Meta:
        db_table = 'topic'

class UserPreference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    id_native_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='native_language_preferences')
    id_language_to_study = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='study_language_preferences')
    id_language_to_study_level = models.ForeignKey(LanguageLevel, on_delete=models.CASCADE)
    id_reason_to_study = models.ForeignKey(ReasonToStudy, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_preference'
        unique_together = ('id_user', 'id_native_language', 'id_language_to_study', 'id_language_to_study_level', 'id_reason_to_study')


class UserPreferenceTopic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user_preference = models.ForeignKey(UserPreference, on_delete=models.CASCADE)
    id_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_preference_topic'
        unique_together = ('id_user_preference', 'id_topic')

class LearningStep(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    des_learning_step = models.CharField(max_length=150)

    class Meta: 
        db_table = 'learning_step'

class LearningPhase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    des_learning_phase = models.CharField(max_length=150)

    class Meta: 
        db_table = 'learning_phase'

class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    id_user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    nam_deck = models.CharField(max_length=256)
    new_cards_per_day = models.PositiveIntegerField(default=0)
    gra_interval = models.PositiveIntegerField(default=24)
    ste_value = models.PositiveIntegerField(default=10)
    gra_max_interval = models.PositiveIntegerField(default=180)

    class Meta: 
        db_table = 'deck'

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    id_last_learning_step = models.ForeignKey(LearningStep, null=True, on_delete=models.CASCADE)
    id_learning_phase = models.ForeignKey(LearningPhase, null=True, on_delete=models.CASCADE)
    lap_card = models.BooleanField(default=False)
    las_interval_card = models.IntegerField(default=0)
    nex_interval_card = models.IntegerField(default=0)
    eas_factor_card = models.IntegerField(default=250)
    val_card = models.CharField(max_length=1000)
    mea_card = models.CharField(max_length=1000)
    day_added_card = models.DateTimeField(null=True)
    fir_review_card = models.DateTimeField(null=True)
    las_review_card = models.DateTimeField(null=True)
    rev_card = models.PositiveIntegerField(default=0)