from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services import (
    get_data,
    matriks_keputusan,
    normalisasi,
    terbobot,
    optimasi,
    ranking,
)


@login_required
def index(request):

    alternatif, kriteria, penilaian = get_data()

    context = {
        "alternatif": alternatif,
        "kriteria": kriteria,
        "penilaian": penilaian,
        "matriks": matriks_keputusan(),
        "normal": normalisasi(),
        "terbobot": terbobot(),
        "optimasi": optimasi(),
        "ranking": ranking(),
    }

    return render(
        request,
        "moora/index.html",
        context
    )