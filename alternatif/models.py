from django.db import models

class Alternatif(models.Model):
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama