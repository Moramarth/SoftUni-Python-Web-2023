from django import forms

from online_library.books.models import Book


class BookForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Description"}))
    image = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Image"}))
    book_type = forms.CharField(label="Type", widget=forms.TextInput(attrs={"placeholder": "Fiction, Novel, Crime.."}))

    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            "belongs_to": forms.HiddenInput()
        }