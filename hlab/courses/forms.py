from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label="name", max_length=120)
    comment = forms.CharField(label="comment", widget=forms.Textarea)
    rating = forms.IntegerField(label="rating out of 5", max_value=5, min_value=1)
