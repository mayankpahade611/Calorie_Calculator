from django import forms
from .models import Userprofile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = [
            "age",
            "gender",
            "height_cm",
            "weight_kg",
            "activity_level",
            "goal",
        ]


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
