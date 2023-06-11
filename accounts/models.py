from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    birth = models.DateField(null=True)
    calories_burned = models.PositiveIntegerField(default=0)
    fit_points = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(null=True)
    completed_goals = models.PositiveIntegerField(default=0)
    active_goals = models.PositiveIntegerField(default=0)

    def clean(self):
        super().clean()
        if not (timezone.now().date() > self.birth):
            raise ValidationError('Invalid birth date!')

