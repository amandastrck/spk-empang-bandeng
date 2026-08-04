from math import sqrt
from collections import defaultdict

from alternatif.models import Alternatif
from kriteria.models import Kriteria
from penilaian.models import Penilaian


# =====================================
# Ambil Data
# =====================================

def get_data():

    alternatif = Alternatif.objects.all()
    kriteria = Kriteria.objects.all()
    penilaian = Penilaian.objects.all()

    return alternatif, kriteria, penilaian


# =====================================
# Matriks Keputusan
# =====================================

def matriks_keputusan():

    penilaian = Penilaian.objects.select_related(
        "alternatif",
        "kriteria",
        "subkriteria"
    )

    matriks = defaultdict(dict)

    for p in penilaian:

        # Menggunakan NAMA alternatif agar tampil lebih jelas
        matriks[p.alternatif.nama][p.kriteria.kode] = float(
            p.subkriteria.skor
        )

    return dict(matriks)


# =====================================
# Normalisasi
# =====================================

def normalisasi():

    matriks = matriks_keputusan()

    kriteria = Kriteria.objects.all()

    pembagi = {}

    for k in kriteria:

        jumlah = 0

        for alt in matriks:

            jumlah += matriks[alt][k.kode] ** 2

        pembagi[k.kode] = sqrt(jumlah)

    hasil = defaultdict(dict)

    for alt in matriks:

        for k in kriteria:

            hasil[alt][k.kode] = round(
                matriks[alt][k.kode] /
                pembagi[k.kode],
                4
            )

    return dict(hasil)


# =====================================
# Matriks Terbobot
# =====================================

def terbobot():

    normal = normalisasi()

    hasil = defaultdict(dict)

    kriteria = Kriteria.objects.all()

    for alt in normal:

        for k in kriteria:

            hasil[alt][k.kode] = round(
                normal[alt][k.kode] *
                float(k.bobot),
                4
            )

    return dict(hasil)


# =====================================
# Nilai Optimasi (Yi)
# =====================================

def optimasi():

    bobot = terbobot()

    kriteria = Kriteria.objects.all()

    hasil = {}

    for alt in bobot:

        benefit = 0
        cost = 0

        for k in kriteria:

            nilai = bobot[alt][k.kode]

            if k.jenis.lower() == "benefit":
                benefit += nilai
            else:
                cost += nilai

        hasil[alt] = round(
            benefit - cost,
            4
        )

    return hasil


# =====================================
# Ranking
# =====================================

def ranking():

    hasil = optimasi()

    ranking = sorted(
        hasil.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranking