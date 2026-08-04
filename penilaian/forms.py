from django import forms

from .models import Penilaian
from subkriteria.models import SubKriteria


class PenilaianForm(forms.ModelForm):

    class Meta:
        model = Penilaian
        fields = "__all__"

        widgets = {
            "alternatif": forms.Select(attrs={"class": "form-control"}),
            "kriteria": forms.Select(attrs={"class": "form-control"}),
            "subkriteria": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # saat pertama dibuka dropdown subkriteria kosong
        self.fields["subkriteria"].queryset = SubKriteria.objects.none()

        # ketika user memilih kriteria
        if "kriteria" in self.data:

            try:

                kriteria_id = int(self.data.get("kriteria"))

                self.fields["subkriteria"].queryset = (
                    SubKriteria.objects.filter(
                        kriteria_id=kriteria_id
                    )
                )

            except (ValueError, TypeError):

                pass

        # ketika edit data
        elif self.instance.pk:

            self.fields["subkriteria"].queryset = (
                SubKriteria.objects.filter(
                    kriteria=self.instance.kriteria
                )
            )