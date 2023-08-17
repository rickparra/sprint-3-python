# -*- coding: utf-8 -*-
"""sprint-3.ipynb
"""

import pandas as pd
import os
import sys
import webbrowser
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

"""##Pandas"""

df = pd.read_csv('dataset.csv')
df.head()

df.isnull().sum()

df['time']

contas = {'henrique': 'rm551973'}


def criar_conta():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    contas[nome] = senha
    print("Conta criada com sucesso!")


def fazer_login():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if nome in contas and contas[nome] == senha:
        print("Login bem-sucedido!")
        segundo_menu(nome)
    else:
        print("Nome de usuário ou senha incorretos.")

def menu():

  continuar = True

  while continuar:

    print("\nMenu:")
    print("1. Criar Conta")
    print("2. Fazer Login")
    print("3. Sair")

    try:
      escolha = int(input("Escolha uma opção: "))
    except ValueError:
      print("Opção inválida. Digite apenas números.")
      continue

    match escolha:
      case 1:
        criar_conta()
      case 2:
        fazer_login()
      case 3:
        print("Desligando...")
        continuar = False
        break  # Encerra o programa imediatamente
      case _:
        print("Opção inválida. Escolha novamente.")

def segundo_menu(nome):

  sair = False

  while not sair:

    print("\nSegundo Menu:")
    print("1. Plotar gráfico de densidade")
    print("2. Plotar gráfico de crimes por ano")
    print("3. Plotar cluster")
    print("4. Sair da conta")

    try:
      escolha = int(input("Escolha uma opção: "))
    except ValueError:
      print("Opção inválida. Digite apenas números.")
      continue

    match escolha:
      case 1:
        print("Gerando gráfico...")
        criar_densidade()

      case 2:
        print("Gerando gráfico...")
        tempo_density()

      case 3:
        print("Gerando gráfico...")
        clusterizar()

      case 4:
        print("Saindo da conta...")
        sair = True




def clusterizar():
    # Agrupar por bairro e calcular médias
    df_agrupado = df.groupby('bairro').agg({'latitude': 'mean',
                                            'longitude': 'mean'}).reset_index()

    # Clusterização
    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(df_agrupado[['latitude', 'longitude']])

    # Adicionar clusters ao dataframe
    df_agrupado['cluster'] = clusters

    # Criar figura interativa
    fig = px.scatter(df_agrupado, x='longitude', y='latitude', color='cluster',
                     title='Clusterização por Bairro', labels={'longitude': 'Longitude', 'latitude': 'Latitude'})

    # Exibir estatisticas por cluster
    # for i in range(3):
    #     print(df_agrupado[df_agrupado.cluster == i].head())

    # Salvar gráfico em um arquivo HTML
    fig.write_html("clusterizacao.html")
    webbrowser.open("clusterizacao.html")


def criar_densidade():

  fig = px.density_mapbox(
      df,
      lat='latitude',
      lon='longitude',
      radius=5,
      zoom=7,
      color_continuous_scale=px.colors.sequential.YlOrRd,
      mapbox_style="stamen-terrain")

  fig.update_layout(
      title='Mapa densidade de crimes',
  )

  html_filename = "densidade.html"
  fig.write_html(html_filename)

  webbrowser.open(os.path.abspath(html_filename))


df['date'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S.%f').dt.year
df=df.sort_values('date')

def tempo_density():
    fig = px.density_mapbox(
        df,
        lat='latitude',
        lon='longitude',
        radius=5,
        zoom=7,
        color_continuous_scale=px.colors.sequential.YlOrRd,
        mapbox_style="stamen-terrain",
        animation_frame='date'
    )

    fig.update_layout(
        title='Mapbox Density Heatmap - Crimes'
    )

    html_filename = "tempo_density.html"
    fig.write_html(html_filename)

    webbrowser.open(os.path.abspath(html_filename))

menu()

