from django.db import models


class Kriteria(models.Model):
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)

    bobot = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    JENIS = (
        ('Benefit', 'Benefit'),
        ('Cost', 'Cost'),
    )

    jenis = models.CharField(
        max_length=10,
        choices=JENIS
    )

    def __str__(self):
        return self.nama