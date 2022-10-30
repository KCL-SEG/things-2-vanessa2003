"""Forms of the project."""
from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'description', 'quantity']
        widgets ={'description': forms.Textarea(), 'quantity':forms.NumberInput() }


# Create your forms here.
