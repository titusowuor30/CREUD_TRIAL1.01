from django import forms
from apps.books.models import Reviews

class RatingForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields=('student','book')