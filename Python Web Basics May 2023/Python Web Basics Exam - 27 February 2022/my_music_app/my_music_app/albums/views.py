from django.shortcuts import render, redirect, get_object_or_404

from my_music_app.accounts.models import Profile
from my_music_app.albums.forms import AlbumForm, AlbumDeleteForm
from my_music_app.albums.models import Album
from my_music_app.common.templatetags.tags import profile_status


# Create your views here.


def add_album(request):
    user = profile_status()
    form = AlbumForm()
    if request.method == "POST":
        data = request.POST.copy()
        data["created_by"] = user.pk
        form = AlbumForm(data)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {"form": form}
    return render(request, "add-album.html", context=context)


def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = {"album": album}
    return render(request, "album-details.html", context=context)


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm(instance=album)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {"form": form}

    return render(request, "edit-album.html", context=context)


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumDeleteForm(instance=album)
    if request.method == "POST":
        album.delete()
        return redirect("home page")
    context = {"form": form}
    return render(request, "delete-album.html", context=context)
