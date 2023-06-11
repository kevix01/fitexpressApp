from django.urls import path
from .views import GoalCreateView, GoalListView, GoalDeleteView, GoalUpdateView, GoalCompleteView


urlpatterns = [
    path("new/", GoalCreateView.as_view(), name="goalnew"),
    path("", GoalListView.as_view(), name="goalslist"),
    path("<int:pk>/delete/", GoalDeleteView.as_view(), name="goaldelete"),
    path("<int:pk>/edit/", GoalUpdateView.as_view(), name="goaledit"),
    path("<int:pk>/complete/", GoalCompleteView.as_view(), name="goalcomplete"),
]
