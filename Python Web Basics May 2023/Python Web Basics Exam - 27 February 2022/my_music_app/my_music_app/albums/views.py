from django.shortcuts import render, redirect, get_object_or_404

from my_music_app.accounts.models import Profile
from my_music_app.albums.forms import AlbumForm, AlbumDeleteForm
from my_music_app.albums.models import Album


# Create your views here.


def add_album(request):
    user = Profile.objects.first()
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
    user = Profile.objects.first()
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm(initial=album.__dict__)
    if request.method == "POST":
        data = request.POST.copy()
        data["created_by"] = user.pk
        form = AlbumForm(data, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {"form": form}

    return render(request, "edit-album.html", context=context)


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumDeleteForm(initial=album.__dict__, instance=album)
    if request.method == "POST":
        album.delete()
        return redirect("home page")
    context = {"form": form}
    return render(request, "delete-album.html", context=context)
