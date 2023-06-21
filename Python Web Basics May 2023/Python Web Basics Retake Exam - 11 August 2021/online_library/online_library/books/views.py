from django.shortcuts import render, redirect, get_object_or_404

from online_library.books.forms import BookForm
from online_library.books.models import Book
from online_library.common.templatetags.tags import profile_status


# Create your views here.


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        user = profile_status()
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
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {"form": form}
    return render(request, "edit-book.html", context)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('home page')
