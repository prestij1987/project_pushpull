from django import forms
from . import models

class ZaprosForm(forms.ModelForm):
    class Meta:
        model = models.Zapros
        fields = [field.name for field in model._meta.get_fields()]
        ''' fields = [
            'deadline',
            'description'
        ]
        labels = {
            "given": "Задача выдана",
        }
        widgets = {
            #'given' :   forms.DateInput(attrs={'type':'datetime-local'}),
            'deadline': forms.DateInput(attrs={'type':'datetime-local'}),
            #'category': forms.TextInput(attrs={'type':'color'}),
        }'''