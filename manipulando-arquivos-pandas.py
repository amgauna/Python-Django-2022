# Python e Pandas - Importação e Exportação de Arquivos

# Manipulando arquivos com Pandas
# Uma das grandes vantagens do Python é a grande facilidade
# e rapidez na abertura e conversão de formatos de arquivos.

No site https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
# você consegue observar a infinidade de arquivos que são passíveis de 
# conversão com Python e Pandas.

# Outro site interessantíssimo que gostaria de compartilhar é o site de
# repositórios https://www.kaggle.com/datasets Neste site é possível baixar 
# datasets de diferentes categorias e assuntos para praticar Data Science.

# Trabalhando com Data Frame
# Importando módulos e Data Frame

import numpy as np
import pandas as pd

df = pd.read_csv("netflix_titles.csv",sep=',')
df.head()
del df['show_id']
df.head()
df.describe()
df.info()

# Vamos agora fazer um exemplo de exportação de dados para outro formato 
# utilizando os métodos to_ do Pandas:

print(df.head(20).to_html())
df[df['country']=='Brazil'].head(20).to_html('netflix.html')

# Podemos também importar dados vindos de um banco de dados de um site ou 
# blog caso ele esteja no formato mysql. Para isso, instalaremos dois módulos:

!pip install sqlalchemy
!pip install pymysql

# E na sequência importá-los no nosso código:

from sqlalchemy import create_engine
import pymysql

# Para fazermos a conexão com o MySql precisamos dos dados do banco e de um 
# servidor de MySql. Na aula nós utilizamos o servidor do Wamp Server. 
# Veja um exemplo de conexão abaixo:

db_connection = create_engine("mysql+pymysql://root:@localhost:3306/wef")
df = pd.read_sql('select * from posts',con=db_connection)
df[df['Id']==42].head()

# Para exportar os dados para o Excel primeiro importamos um módulo e depois
# efetivamos a exportação:

!pip install openpyxl
df.to_excel('db.xlsx')

# Com Pandas também é possível trazer dados de tabelas de sites externos.

!pip install lxml
df = pd.read_html("https://www.w3schools.com/html/html_tables.asp")
df

