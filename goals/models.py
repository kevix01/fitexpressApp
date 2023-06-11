from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Goals(models.Model):
    class GoalTypes(models.TextChoices):
        LOSE_WEIGHT = "LOSE WEIGHT", "LOSE WEIGHT"
        MUSCLE_STRENGTH = "MUSCLE STRENGTH", "MUSCLE STRENGTH"
        MUSCLE_MASS = "MUSCLE MASS", "MUSCLE MASS"
        BODY_DEFINITION = "BODY DEFINITION", "BODY DEFINITION"
        CARDIO = "CARDIO", "CARDIO"

    goal_type = models.TextField(choices=GoalTypes.choices)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.TextField(default="Active")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    creation_date = models.DateField(auto_now_add=True)
    estimated_finish_date = models.DateField()
    complete_date = models.DateField(null=True)

    def clean(self):
        super().clean()
        if not (timezone.now().date() <= self.estimated_finish_date):
            raise ValidationError('Estimated finish date must be greater or equals today!')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("goalslist")
