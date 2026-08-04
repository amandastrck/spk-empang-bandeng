from django import forms
from .models import SubKriteria


class SubKriteriaForm(forms.ModelForm):

    class Meta:
        model = SubKriteria
        fields = '__all__'

        widgets = {
            'kriteria': forms.Select(attrs={
                'class': 'form-control'
            }),

            'deskripsi': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'skor': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }