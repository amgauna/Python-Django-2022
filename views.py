# No arquivo views implementamos a lógica da aplicação, inclusive usando o Pandas e o Numpy.

from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd

# Create your views here.

def home(request):
    df = pd.read_csv('app/static/data/netflix_titles.csv')
    data = {}
    data['dados']=df.head().to_html()
    return render(request,'index.html',data)
