from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="penilaian"),
    path("tambah/", views.tambah, name="tambah_penilaian"),
    path("edit/<int:id>/", views.edit, name="edit_penilaian"),
    path("hapus/<int:id>/", views.hapus, name="hapus_penilaian"),

    path(
        "get-subkriteria/",
        views.get_subkriteria,
        name="get_subkriteria"
    ),
]