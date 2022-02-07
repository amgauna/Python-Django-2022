project/urls.py

# Vamos setar a url do nosso app:

from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
