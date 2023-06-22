from django.shortcuts import render, redirect, get_object_or_404

from notes_app.common.templatetags.tags import profile_status
from notes_app.notes.forms import NoteForm, NoteDeleteForm
from notes_app.notes.models import Note


# Create your views here.


def add_note(request):
    form = NoteForm()
    if request.method == "POST":
        user = profile_status()
        data = request.POST.copy()
        data["created_by"] = user.pk
        form = NoteForm(data)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {"form": form}
    return render(request, "note-create.html", context)


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {"form": form}
    return render(request, "note-edit.html", context)


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteDeleteForm(instance=note)
    if request.method == "POST":
        note.delete()
        return redirect("home_page")
    context = {"form": form}
    return render(request, "note-delete.html", context)


def note_details(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {"note": note}
    return render(request, "note-details.html", context)
