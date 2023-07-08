from django.db import models
from hello.utils.SelfDescriptionMixin import SelfDescriptionMixin


class Question(SelfDescriptionMixin, models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')
    multiple = models.BooleanField(default=False)
    text = models.BooleanField(default=False)


class Choice(SelfDescriptionMixin, models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=140)
    votes = models.IntegerField(default=0)
