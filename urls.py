project/urls.py

# Vamos setar a url do nosso app:

from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

# Vamos criar a rota para filtragem de países:

from django.contrib import admin
from django.urls import path
from app.views import home,countryFilter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('countryFilter/', countryFilter),
]

# Vamos criar a rota dos detalhes:

from django.contrib import admin
from django.urls import path
from app.views import home,countryFilter,detalhes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('countryFilter/', countryFilter),
    path('detalhes//', detalhes),
]

