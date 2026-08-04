from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Penilaian
from .forms import PenilaianForm

from subkriteria.models import SubKriteria


@login_required
def index(request):

    data = Penilaian.objects.all()

    return render(
        request,
        "penilaian/index.html",
        {
            "data": data
        }
    )


@login_required
def tambah(request):

    form = PenilaianForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect("penilaian")

    return render(
        request,
        "penilaian/tambah.html",
        {
            "form": form
        }
    )


@login_required
def edit(request, id):

    data = get_object_or_404(
        Penilaian,
        id=id
    )

    form = PenilaianForm(
        request.POST or None,
        instance=data
    )

    if form.is_valid():

        form.save()

        return redirect("penilaian")

    return render(
        request,
        "penilaian/edit.html",
        {
            "form": form
        }
    )


@login_required
def hapus(request, id):

    data = get_object_or_404(
        Penilaian,
        id=id
    )

    data.delete()

    return redirect("penilaian")


# ===========================
# AJAX Dropdown Sub Kriteria
# ===========================

@login_required
def get_subkriteria(request):

    kriteria_id = request.GET.get("kriteria")

    data = SubKriteria.objects.filter(
        kriteria_id=kriteria_id
    ).values(
        "id",
        "deskripsi"
    )

    return JsonResponse(
        list(data),
        safe=False
    )