from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profil


@login_required
def index(request):

    profil = Profil.objects.first()

    context = {
        "profil": profil
    }

    return render(
        request,
        "profil/index.html",
        context
    )