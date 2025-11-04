from django.urls import path

from . import views

app_name = "studylog"

urlpatterns = [
    path("", views.subject_list, name="subject_list"),
    path("subjects/add/", views.add_subject, name="add_subject"),
    path("subjects/<int:pk>/", views.subject_detail, name="subject_detail"),
    path("subjects/<int:pk>/entries/add/", views.add_entry, name="add_entry"),
]
