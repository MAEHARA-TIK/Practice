from django.contrib import admin

from .models import StudyEntry, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(StudyEntry)
class StudyEntryAdmin(admin.ModelAdmin):
    list_display = ("subject", "study_date", "duration_minutes", "created_at")
    list_filter = ("subject", "study_date")
    search_fields = ("subject__name", "notes")
