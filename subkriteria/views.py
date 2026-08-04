from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import SubKriteria
from .forms import SubKriteriaForm


@login_required
def index(request):

    data = SubKriteria.objects.all()

    context = {
        "data": data
    }

    return render(
        request,
        "subkriteria/index.html",
        context
    )


@login_required
def tambah(request):

    form = SubKriteriaForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect("subkriteria")

    context = {
        "form": form
    }

    return render(
        request,
        "subkriteria/tambah.html",
        context
    )


@login_required
def edit(request, id):

    data = get_object_or_404(
        SubKriteria,
        id=id
    )

    form = SubKriteriaForm(
        request.POST or None,
        instance=data
    )

    if form.is_valid():

        form.save()

        return redirect("subkriteria")

    context = {
        "form": form
    }

    return render(
        request,
        "subkriteria/edit.html",
        context
    )


@login_required
def hapus(request, id):

    data = get_object_or_404(
        SubKriteria,
        id=id
    )

    data.delete()

    return redirect("subkriteria")