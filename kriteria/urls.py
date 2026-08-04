from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="kriteria"),

    path("tambah/", views.tambah, name="tambah_kriteria"),

    path("edit/<int:id>/", views.edit, name="edit_kriteria"),

    path("hapus/<int:id>/", views.hapus, name="hapus_kriteria"),

]