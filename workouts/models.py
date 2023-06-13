from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Workout(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    exercise_num = models.PositiveIntegerField(default=0)
    last_training_date = models.DateField(null=True, blank=True)
    kcal = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_author(self):
        return self.author.__str__()

    def get_absolute_url(self):
        return reverse("workoutexercises", kwargs={"workout_pk": self.pk})


class MuscleGroups(models.TextChoices):
    BACK = "BACK", "BACK"
    SHOULDERS = "SHOULDERS", "SHOULDERS"
    ABDOMEN = "ABDOMEN", "ABDOMEN"
    CHEST = "CHEST", "CHEST"
    LEGS = "LEGS", "LEGS"
    ARMS = "ARMS", "ARMS"


class Exercises(models.Model):
    muscle_group = models.TextField(choices=MuscleGroups.choices)
    title = models.CharField(max_length=255)
    kcal_rep = models.PositiveIntegerField()

    def __str__(self):
        return self.title + " [Category: " + self.muscle_group + "]"


class WorkoutExercises(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField()
    kcal_tot = models.PositiveIntegerField()

    def clean(self):
        super().clean()
        if not (self.repetitions > 0):
            raise ValidationError('Repetitions number must be greater than zero!')

    def get_absolute_url(self):
        return reverse("workoutexercises", kwargs={"workout_pk": self.workout.pk})

