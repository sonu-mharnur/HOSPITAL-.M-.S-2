from django import forms
from .models import hospitaldata

class hospitalForm(forms.ModelForm):
    class Meta:
        model = hospitaldata
        fields = '__all__'