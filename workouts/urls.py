from django.urls import path

from .views import (
    WorkoutListView,
    WorkoutUpdateView,
    WorkoutDeleteView,
    WorkoutCreateView,
    WorkoutExercisesView,
    WorkoutExerciseEdit,
    WorkoutExerciseCreateView,
    WorkoutExerciseDeleteView,
    WorkoutTrainView,
    WorkoutStandardListView
)

urlpatterns = [
    path("<int:workout_pk>/", WorkoutExercisesView.as_view(), name="workoutexercises"),
    path("<int:pk>/train", WorkoutTrainView.as_view(), name="workouttrain"),
    path("<int:pk>/edit/", WorkoutUpdateView.as_view(), name="workoutedit"),
    path("<int:pk>/delete/", WorkoutDeleteView.as_view(), name="workoutdelete"),
    path("new/", WorkoutCreateView.as_view(), name="workoutnew"),
    path("<int:workout_pk>/<int:pk>/delete/", WorkoutExerciseDeleteView.as_view(), name="workoutexercise_delete"),
    path("<int:workout_pk>/<int:pk>/edit/", WorkoutExerciseEdit.as_view(), name="workoutexercise_edit"),
    path("<int:pk>/addexercise", WorkoutExerciseCreateView.as_view(), name="workoutexercise_new"),
    path("myworkouts/", WorkoutListView.as_view(), name="workoutlist"),
    path("", WorkoutStandardListView.as_view(), name="workoutstandardlist"),
]
