from django.shortcuts import render, redirect, get_object_or_404

from online_library.accounts.models import Profile
from online_library.books.forms import BookForm
from online_library.books.models import Book


# Create your views here.


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        user = Profile.objects.first()
        data = request.POST.copy()
        data["belongs_to"] = user.pk
        form = BookForm(data)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {"form": form}
    return render(request, "add-book.html", context)


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, "book-details.html", context)


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(initial=book.__dict__)
    if request.method == "POST":
        user = Profile.objects.first()
        data = request.POST.copy()
        data["belongs_to"] = user.pk
        form = BookForm(data, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {"form": form}
    return render(request, "edit-book.html", context)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('home page')
