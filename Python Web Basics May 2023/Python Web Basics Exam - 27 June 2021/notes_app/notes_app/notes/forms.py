from django import forms

from notes_app.notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        widgets = {
            "created_by": forms.HiddenInput()
        }

        labels = {
            "image_url": "Link to Image"
        }


class NoteDeleteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"
