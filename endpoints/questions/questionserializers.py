
from rest_framework import serializers
from .models import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Questions
            fields = ('courseid ', 'section', 'data')
