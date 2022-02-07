# Pandas Plot e Plotly

# Métodos de Plotagem do Pandas
# Veja abaixo alguns métodos que podem ser usados para plotagem de gráficos 
# usando o próprio Pandas. No exemplo vamos usar o DataFrame flights.csv.

df.hist()
df['passengers'].plot.area()
df['passengers'].plot.bar()
df.plot.scatter(x='year',y='passengers',c='year')
df.plot.line(x='year',y='passengers')
df['year'].plot.box()

# Lib Plotly Python
# Para trabalhar com o Plotly precisamos primeiramente instalar a lib na nossa venv:

pip install plotly==5.1.0
pip install "jupyterlab>=3" "ipywidgets>=7.6"

# Bora agora importar os módulos e iniciar a plotagem de gráficos. 
# Neste exemplo trabalhareos com o Data Frame tips.csv

import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

df = pd.read_csv("tips.csv")
df.head()

trace = go.Scatter(x=df['total_bill'],y=df['tip'],mode='markers')
data = [trace]
py.iplot(data)

group = df.groupby('sex')
trace = go.Bar(x = df['sex'].unique(), y = group['total_bill'].count())
data = [trace]
py.iplot(data)

