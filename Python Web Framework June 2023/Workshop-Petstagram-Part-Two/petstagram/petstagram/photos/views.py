import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.

@login_required
def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        photo = form.save()
        photo.user = request.user
        photo.save()
        return redirect('home page')
    context = {
        "form": form,
    }
    return render(request, template_name='photos/photo-add-page.html', context=context)


@login_required
def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    photo_is_liked_by_user = likes.filter(user=request.user)
    comments = photo.comment_set.all()
    comment_form = CommentForm()
    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
        "comment_form": comment_form,
        "photo_is_liked_by_user": photo_is_liked_by_user,

    }
    return render(request, template_name='photos/photo-details-page.html', context=context)


@login_required
def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == "POST":
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)

    form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    context = {
        "form": form,
    }
    return render(request, template_name='photos/photo-edit-page.html', context=context)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo_path = os.path.join('media/', str(photo.photo))
    os.remove(photo_path)
    photo.delete()

    return redirect("home page")
