from django.shortcuts import render

# Create your views here.


def add_note(request):
    return render(request, "note-create.html")\



def edit_note(request, pk):
    return render(request, "note-edit.html")


def delete_note(request, pk):
    return render(request, "note-delete.html")


def note_details(request, pk):
    return render(request, "note-details.html")
