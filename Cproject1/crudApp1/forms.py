from django import forms
from .models import voters

class votersForm(forms.ModelForm):
    class Meta:
        model = voters
        fields = '__all__'

        widgets = {
            'dob': forms.DateInput(attrs={'type':'date'})
        }