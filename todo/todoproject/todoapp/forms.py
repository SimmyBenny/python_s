from . models import task
from django import forms

class uptask(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','pr','date']