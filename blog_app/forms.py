from django import forms
from .models import Post, Comment, Reel

class PostForm(forms.ModelForm):
    class Meta:
        model =  Post
        fields = [
            "title",
            "article",
            "description"
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment_body"
        ]

class ReelForm(forms.ModelForm):
    class Meta:
        model = Reel
        fields = [
           "description" 
        ]