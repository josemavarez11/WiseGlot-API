from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.middlewares import admin_required, jwt_required
from .serializers import DeckSerializer, CardSerializer, LearningPhaseSerializer, LearningStepSerializer
from .models import Deck, Card, LearningPhase, LearningStep

# Create your views here.
