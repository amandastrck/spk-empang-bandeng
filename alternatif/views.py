from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Alternatif
from .forms import AlternatifForm


@login_required
def index(request):

    data = Alternatif.objects.all()

    context = {
        "data": data
    }

    return render(
        request,
        "alternatif/index.html",
        context
    )


@login_required
def tambah(request):

    form = AlternatifForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("alternatif")

    context = {
        "form": form
    }

    return render(
        request,
        "alternatif/tambah.html",
        context
    )


@login_required
def edit(request, id):

    alternatif = Alternatif.objects.get(id=id)

    form = AlternatifForm(
        request.POST or None,
        instance=alternatif
    )

    if form.is_valid():
        form.save()
        return redirect("alternatif")

    context = {
        "form": form
    }

    return render(
        request,
        "alternatif/edit.html",
        context
    )


@login_required
def hapus(request, id):

    alternatif = Alternatif.objects.get(id=id)

    alternatif.delete()

    return redirect("alternatif")