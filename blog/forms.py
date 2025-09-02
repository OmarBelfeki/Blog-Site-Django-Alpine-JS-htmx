# blog/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]
        widgets = {
            "author": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "text": forms.Textarea(attrs={"class": "textarea textarea-bordered w-full"}),
        }
