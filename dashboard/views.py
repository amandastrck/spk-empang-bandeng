from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from alternatif.models import Alternatif
from kriteria.models import Kriteria
from penilaian.models import Penilaian

from moora.services import ranking


@login_required
def index(request):

    hasil = ranking()

    terbaik = hasil[0] if hasil else None

    context = {

        "jumlah_alternatif": Alternatif.objects.count(),

        "jumlah_kriteria": Kriteria.objects.count(),

        "jumlah_penilaian": Penilaian.objects.count(),

        "terbaik": terbaik,

        "ranking": hasil,

    }

    return render(

        request,

        "dashboard/index.html",

        context

    )