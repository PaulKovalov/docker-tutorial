from django.db import models

# Create your models here.


class Poll(models.Model):
    header = models.CharField(default='', max_length=200)


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(default='', max_length=200)


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    text = models.CharField(default='', max_length=200)
