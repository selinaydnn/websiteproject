from django.db import models
class Questionnaire(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
class Question(models.Model):
    TYPE_CHOICES = [
        ('MCQ', 'Multiple Choice Question'),
        ('TF', 'True/False'),
        ('TEXT', 'Text-based Answer'),
        # Add more types as needed
    ]

    text = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text
