import pandas as pd
import plotly.express as px
import streamlit as st

# Ler os dados
car_data = pd.read_csv('vehicles_us.csv')

# Título do aplicativo
st.title('Análise de Anúncios de Carros Usados')

# Botão para exibir histograma
if st.button('Mostrar histograma do odômetro'):
    st.write('Histograma: distribuição da quilometragem dos carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para exibir gráfico de dispersão
if st.button('Mostrar gráfico de dispersão odômetro vs preço'):
    st.write('Gráfico de dispersão: quilometragem vs preço')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
