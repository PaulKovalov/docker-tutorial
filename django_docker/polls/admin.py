from django.contrib import admin
from .models import Question, Poll, AnswerOption

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(AnswerOption)
