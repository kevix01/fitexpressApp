from django.contrib import admin
from django.urls import path, include

from django_project.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("workouts/", include("workouts.urls")),
    path("goals/", include("goals.urls")),
]
