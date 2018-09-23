from django.shortcuts import render
from rest_framework import viewsets
from endpoints.users.models import Users
#from endpoints.courses.models import Users
from .questionserializers import QuestionsSerializer
from .models import Questions
# Create your views here.
class QuestionView (viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


    ## crud if user is professor
    ## crud operations




    ##if user is student
    ## post answer