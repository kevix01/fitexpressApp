from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "pk",
        "email",
        "username",
        "birth",
        "weight",
        "is_staff",
        "fit_points",
        "calories_burned",
        "active_goals",
        "completed_goals"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("birth",
                                                          "weight",
                                                          "fit_points",
                                                          "calories_burned",
                                                          "active_goals",
                                                          "completed_goals")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("birth",
                                                                  "weight",
                                                                  "fit_points",
                                                                  "calories_burned",
                                                                  "active_goals",
                                                                  "completed_goals")}),)


admin.site.register(CustomUser, CustomUserAdmin)
