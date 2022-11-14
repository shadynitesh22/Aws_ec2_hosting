from django.forms import ModelForm

from .models import Author, RandomModel


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
