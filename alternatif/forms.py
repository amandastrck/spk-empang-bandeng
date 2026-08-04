from django import forms
from .models import Alternatif

class AlternatifForm(forms.ModelForm):

    class Meta:
        model = Alternatif
        fields = ['kode', 'nama']