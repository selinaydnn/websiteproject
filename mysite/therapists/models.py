from django.db import models

class Therapist(models.Model):
    # Other fields...
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
