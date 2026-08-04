from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("login/", include("accounts.urls")),

    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),

    path("alternatif/", include("alternatif.urls")),

    path("kriteria/", include("kriteria.urls")),

    path("subkriteria/", include("subkriteria.urls")),

    path("penilaian/", include("penilaian.urls")),

    path("moora/", include("moora.urls")),

    path("laporan/", include("laporan.urls")),

    path("profil/", include("profil.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)