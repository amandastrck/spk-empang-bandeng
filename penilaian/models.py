from django.db import models
from alternatif.models import Alternatif
from kriteria.models import Kriteria
from subkriteria.models import SubKriteria


class Penilaian(models.Model):
    alternatif = models.ForeignKey(
        Alternatif,
        on_delete=models.CASCADE
    )

    kriteria = models.ForeignKey(
        Kriteria,
        on_delete=models.CASCADE
    )

    subkriteria = models.ForeignKey(
        SubKriteria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.alternatif} - {self.kriteria}"