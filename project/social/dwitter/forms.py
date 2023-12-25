# dwitter/forms.py

# dwitter/forms.py

from django import forms
from .models import Dweet
# users/forms.py

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Post something...",
                "class": "textarea  is-medium",
            }
        ),
        label="",
    )
    

    class Meta:
        model = Dweet
        exclude = ("user", )
