from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First name', max_length=50, widget=forms.widgets.TextInput(
        attrs={
            "class": "form-control"
        }
    ))

    last_name = forms.CharField(label='Last name', max_length=50, widget=forms.widgets.TextInput(
        attrs={
            "class": "form-control"
        }
    ))

    email = forms.EmailField(label='Email', widget=forms.widgets.EmailInput(
        attrs={
            "class": "form-control"
        }
    ))

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)



class ProfileForm(forms.ModelForm):
    picture = forms.ImageField()
    bio = forms.CharField(widget=forms.widgets.Textarea(
        attrs={
            "placeholder":"Tell us about yourself...",
            "class":"form-control text-muted"
        }
    ))

    class Meta:
        model = Profile
        fields = ('picture', 'bio',)
