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

