from django.shortcuts import render

# Create your views here.


def add_book(request):
    return render(request, "add-book.html")


def book_details(request, pk):
    return render(request, "book-details.html")


def edit_book(request, pk):
    return render(request, "edit-book.html")
