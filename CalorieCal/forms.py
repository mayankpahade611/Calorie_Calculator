from django import forms
from .models import Userprofile

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