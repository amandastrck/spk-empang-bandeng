from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Kriteria
from .forms import KriteriaForm


@login_required
def index(request):

    data = Kriteria.objects.all()

    context = {
        "data": data
    }

    return render(
        request,
        "kriteria/index.html",
        context
    )


@login_required
def tambah(request):

    form = KriteriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("kriteria")

    context = {
        "form": form
    }

    return render(
        request,
        "kriteria/tambah.html",
        context
    )


@login_required
def edit(request, id):

    data = Kriteria.objects.get(id=id)

    form = KriteriaForm(
        request.POST or None,
        instance=data
    )

    if form.is_valid():
        form.save()
        return redirect("kriteria")

    context = {
        "form": form
    }

    return render(
        request,
        "kriteria/edit.html",
        context
    )


@login_required
def hapus(request, id):

    data = Kriteria.objects.get(id=id)

    data.delete()

    return redirect("kriteria")