from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import StudyEntryForm, SubjectForm
from .models import Subject


def subject_list(request):
    """Display all subjects with their accumulated study time."""
    subjects = Subject.objects.annotate(total_minutes=Sum("entries__duration_minutes"))
    context = {
        "subjects": subjects,
        "subject_form": SubjectForm(),
    }
    return render(request, "studylog/subject_list.html", context)


def subject_detail(request, pk):
    """Show a single subject and its study entries."""
    subject = get_object_or_404(
        Subject.objects.prefetch_related("entries"), pk=pk
    )
    entry_form = StudyEntryForm()
    entries = subject.entries.all()
    total_minutes = entries.aggregate(total=Sum("duration_minutes"))["total"] or 0
    context = {
        "subject": subject,
        "entry_form": entry_form,
        "entries": entries,
        "total_minutes": total_minutes,
    }
    return render(request, "studylog/subject_detail.html", context)


def add_subject(request):
    """Handle creation of a new subject."""
    if request.method != "POST":
        return redirect("studylog:subject_list")

    form = SubjectForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("studylog:subject_list")


def add_entry(request, pk):
    """Handle creation of a new study entry for a subject."""
    subject = get_object_or_404(Subject, pk=pk)
    if request.method != "POST":
        return redirect("studylog:subject_detail", pk=subject.pk)

    form = StudyEntryForm(request.POST)
    if form.is_valid():
        entry = form.save(commit=False)
        entry.subject = subject
        entry.save()
    return redirect(reverse("studylog:subject_detail", kwargs={"pk": subject.pk}))


