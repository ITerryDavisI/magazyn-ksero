from django import forms
from .models import Copier

class CopierForm(forms.ModelForm):
    class Meta:
        model = Copier
        fields = [
            'brand',
            'model',
            'serial_number',
            'total_counter',
            'mono_counter',
            'color_counter',
             'ready',
             'notes',
        ]
