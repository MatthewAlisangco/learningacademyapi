from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class Questions(models.Model):
    courseid = models.CharField(max_length=20)
    section = models.CharField(max_length=100)
    #data multiple choice {title , description: {questiontype:multi , question: " " , choices: choices.array , answer choices.index[x]}
    # data plaintext {title , tags, description: {questiontype:plaintext , question: " " , answer: " "}
    data = JSONField()