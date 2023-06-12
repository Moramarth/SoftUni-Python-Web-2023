from django.shortcuts import render

from Petstagram.photos.models import Photo


# Create your views here.


def add_photo(request):
    return render(request, template_name='photos/photo-add-page.html')


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,

    }
    return render(request, template_name='photos/photo-details-page.html', context=context)


def edit_photo(request, pk):
    return render(request, template_name='photos/photo-edit-page.html')
