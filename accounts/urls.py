from django.urls import path
from .views import SignUpView, WeightEdit

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<slug:pk>/updateweight/", WeightEdit.as_view(), name="weightupdate")
]
