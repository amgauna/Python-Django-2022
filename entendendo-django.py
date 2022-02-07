# Entendendo o Django
# Hoje iniciamos o conhecimento sobre o framework de Python Django. 
# Vamos entender um pouco sobre rotas, template engine e arquitetura de software do Django.

# Requisitos pra trabalhar com Django
# No terminal de comandos vamos rodar os seguintes comandos:

cd c:/
mkdir Python
cd Python
python -m venv venv
cd venv/Scripts
activate
cd c:/
pip install django
django-admin startproject project .
python manage.py startapp app
project/settings.py

# Precisamos adicionar o app recém criado a lista de apps do projeto:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]
project/urls.py

# Vamos setar a url do nosso app:

from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
app/views.py

# Agora já entrando no app vamos até o arquivo views setar a função home:

from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello World')

# Rode no terminal o comando:

python manage.py runserver

# Depois basta acessar no seu navegador http://localhost:8000, se aparecer a mensagem
# Hello World quer dizer que seu sistema já está configurado para começar o CRUD.

