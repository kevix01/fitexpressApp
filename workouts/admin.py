from django.contrib import admin
from .models import Workout, Exercises, WorkoutExercises


class WorkoutAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "description",
        "author",
    ]


class ExercisesAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "muscle_group",
        "kcal_rep",
    ]


class WorkoutExercisesAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "workout_id",
        "exercise_id",
        "repetitions",
        "kcal_tot",
    ]


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercises, ExercisesAdmin)
admin.site.register(WorkoutExercises, WorkoutExercisesAdmin)
