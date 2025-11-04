from django import forms

from .models import StudyEntry, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "例) 英語リーディング"}),
            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control",
                    "placeholder": "重点ポイントや使用教材などをメモできます",
                }
            ),
        }


class StudyEntryForm(forms.ModelForm):
    class Meta:
        model = StudyEntry
        fields = ["study_date", "duration_minutes", "notes"]
        widgets = {
            "study_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "duration_minutes": forms.NumberInput(
                attrs={"class": "form-control", "min": 0, "step": 5, "placeholder": "学習時間(分)"}
            ),
            "notes": forms.Textarea(
                attrs={"rows": 3, "class": "form-control", "placeholder": "学習内容、気づきなどを記録"}
            ),
        }
