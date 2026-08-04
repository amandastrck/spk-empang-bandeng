from django import forms
from .models import Kriteria

class KriteriaForm(forms.ModelForm):

    class Meta:
        model = Kriteria
        fields = '__all__'

        widgets = {
            'kode': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'bobot': forms.NumberInput(attrs={'class': 'form-control'}),
            'jenis': forms.Select(attrs={'class': 'form-control'}),
        }