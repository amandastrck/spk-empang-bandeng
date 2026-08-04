from django.db import models


class Profil(models.Model):

    nama_usaha = models.CharField(max_length=200)

    pemilik = models.CharField(max_length=200)

    alamat = models.TextField()

    luas = models.CharField(max_length=100)

    tahun_berdiri = models.PositiveIntegerField()

    komoditas = models.CharField(max_length=100)

    deskripsi = models.TextField()

    foto = models.ImageField(
        upload_to="profil/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nama_usaha