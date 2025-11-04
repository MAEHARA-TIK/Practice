from datetime import date

from django.db import models


class Subject(models.Model):
    """Study subject or topic the user wants to track."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class StudyEntry(models.Model):
    """A single study session log tied to a subject."""

    subject = models.ForeignKey(
        Subject,
        related_name="entries",
        on_delete=models.CASCADE,
    )
    study_date = models.DateField(default=date.today)
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-study_date", "-created_at"]

    def __str__(self) -> str:
        return f"{self.subject.name} - {self.study_date}"
