import pandas as pd
import streamlit as st
#import plotly.express as px
#import numpy as np
#import matplotlib.pyplot as plt
#import time

st.set_page_config(layout='wide')

st.title("Dashboard com Streamlit")
st.subheader("Explorando visualizações simples com streamlit")
st.write("Este é um exemplo simples de como criar um app com o Streamlit.")

url = "https://raw.githubusercontent.com/mathe-u/datasets/main/despesas.csv"

@st.cache_data
def load_data(url):
  df = pd.read_csv(url)
  return df

df = load_data(url)

st.sidebar.title("Filtros")
filhos_sidebar = st.sidebar.selectbox('Selecione a quantidade de filhos', df['filhos'].unique())
regiao_sidebar = st.sidebar.selectbox('Selecione a região', df['regiao'].unique())

df_filtrado = df[ 
  (df['filhos'] == filhos_sidebar) & 
  (df['regiao'] == regiao_sidebar)
]

col1, col2 = st.columns(2)

with col1:
  st.write("Dataframe na primeira coluna:")
  st.write(df_filtrado)
  
with col2:
  st.write("Grafico na segunda coluna:")
  df_media_gastos = df_filtrado.groupby('sexo')['gastos'].mean().reset_index()
  st.bar_chart(df_media_gastos, x='sexo', y='gastos', y_label='Media de gastos', color='sexo')

df_media = df_filtrado.groupby('sexo').agg({
    'bmi': 'mean',
    'idade': 'mean',
    'fumantes': lambda x: (x == 'sim').sum()
}).reset_index()

st.write("Visualização das Médias:")

col3, col4, col5 = st.columns(3)

with col3:
  st.bar_chart(df_media, x='sexo', y='bmi', y_label='Média BMI', color='sexo')

with col4:
  st.bar_chart(df_media, x='sexo', y='idade', y_label='Média de Idade', color='sexo')

with col5:
  st.bar_chart(df_media, x='sexo', y='fumantes', color='sexo')
