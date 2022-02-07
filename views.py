# No arquivo views implementamos a lógica da aplicação, inclusive usando o Pandas e o Numpy.
# Vamos testar o uso dos métodos do Pandas para manipular nossos dados:
# Agora já entrando no app vamos até o arquivo views setar a função home:

from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd

# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def replaceCountries(x):
    if(x=='Brazil'):
        return x.replace('Brazil','Brasil')
    else:
        return x

def home(request):
    df = pd.read_csv('app/static/data/netflix_titles.csv')
    data = {}
    #print(df.count())
    #print(df.info())
    """data['dados']=df[(df['release_year']>2009) & (df['country']=='Brazil')]\
        .drop(['show_id','date_added'],axis=1)\
        .dropna()\
        .head(20)\
        .to_html(index=False,classes=['table','table-striped','mt-5'])"""
    #print(data['dados'].count())

    """df['country'] = df['country'].apply(replaceCountries)
    data['dados'] = df.to_html(index=False, classes=['table', 'table-striped', 'mt-5'])"""

    grupo=df.groupby('country').count()
    data['dados']=grupo[['title','release_year']]\
        .sort_values(by='title',ascending=False)\
        .to_html()
    return render(request,'index.html',data)

# Ajax e Pandas
# app/views.py
# Vamos preparar primeiramente a views para que ela realize o filtro e envie os dados para o template:

from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from django.http import JsonResponse
import pandas as pd
import json

df = pd.read_csv('app/static/data/netflix_titles.csv')
data = {}

#Template da Home
def home(request):
    #data['dados']=df[(df['release_year']>2009) & (df['country']=='Brazil')]\
    data['dados']=df\
        .drop(['show_id','date_added'],axis=1)\
        .dropna()\
        .head(20)\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
    data['countryFilter']=df['country'].sort_values().unique()
    return render(request,'index.html',data)

#Requisição para filtro de país
def countryFilter(request):
    if request.body:
        field = json.loads(request.body.decode('utf-8'))
        search = field['country']
        df2=df.dropna()
        data['dados']=df2[df2['country'].str.contains(search)]\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
        return JsonResponse({'data':data['dados']})
    
 # Vamos fazer a filtragem através do Pandas na nossa views:

def countryFilter(request):
    if request.body:
        field = json.loads(request.body.decode('utf-8'))
        search = field['country']
        title = field['title']
        df2=df.dropna()
        data['dados']=df2[(df2['country'].str.contains(search))&(df2['title'].str.contains(title,flags=re.IGNORECASE))]\
        .to_html(index=False,classes=['table','table-striped','mt-5'])
        return JsonResponse({'data':data['dados']})
    
