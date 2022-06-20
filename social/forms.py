from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={
            'placeholder': 'Add a comment...',
            'class': 'form-control text-muted',
        }
    ), label="")

    class Meta:
        model = Comment
        exclude = ("user", "post", )


class PostForm(forms.ModelForm):
    image = forms.ImageField(label="", widget=forms.widgets.FileInput(attrs={'class':'form-control form-control-lg p-0'}))
    caption = forms.CharField(required=False,  label="", widget=forms.widgets.Textarea(
        attrs={
            'placeholder': 'Add a caption...',
            'class': 'form-control text-muted',
        }
    ))

    class Meta:
        model = Post
        exclude = ("user", "likes", )