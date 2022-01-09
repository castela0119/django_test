from datetime import datetime
from django.db import models
from django.db.models.fields import DateField

from django.db import models
from django.utils import timezone

# Create your models here.
# 데이터 타입에 관련된 리스트도 장고 문서에 있으니 참고할 것!

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text