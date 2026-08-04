from django.db import models
from kriteria.models import Kriteria

class SubKriteria(models.Model):
    kriteria = models.ForeignKey(
        Kriteria,
        on_delete=models.CASCADE
    )

    deskripsi = models.CharField(max_length=100)

    skor = models.IntegerField()

    def __str__(self):
        return self.deskripsi