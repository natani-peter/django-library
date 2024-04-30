from django import forms
from . import models


class BookReviewForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=5, min_value=1, widget=forms.NumberInput())

    class Meta:
        model = models.Review
        fields = ['rating', 'description']


class StatusForm(forms.ModelForm):
    class Meta:
        model = models.LibrayRecords
        fields = ['return_status']
