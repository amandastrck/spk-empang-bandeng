from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="alternatif"),

    path("tambah/", views.tambah, name="tambah_alternatif"),

    path("edit/<int:id>/", views.edit, name="edit_alternatif"),
    
    path("hapus/<int:id>/", views.hapus, name="hapus_alternatif"),
]