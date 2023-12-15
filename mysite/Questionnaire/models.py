from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def _str_(self):
        return self.question_text

class Answer(models.Model):
    answer_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def _str_(self):
        return self.answer_text