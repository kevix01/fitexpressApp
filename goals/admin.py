from django.contrib import admin

from goals.models import Goals


class GoalsAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "description",
        "author",
        "goal_type",
        "creation_date",
        "estimated_finish_date",
    ]


admin.site.register(Goals, GoalsAdmin)

# Register your models here.
