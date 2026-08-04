from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='subkriteria'),

    path('tambah/', views.tambah, name='tambah_subkriteria'),

    path('edit/<int:id>/', views.edit, name='edit_subkriteria'),

    path('hapus/<int:id>/', views.hapus, name='hapus_subkriteria'),

]