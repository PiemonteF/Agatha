import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

st.markdown("<h1 style='text-align: center; color: Black;'>Sobre o Projeto</h1>", unsafe_allow_html=True)

st.write('Inicia-se um resumo de como foi realizado o modelo Agatha, machine learning produzida com objetivo de predizer o melhor tratamento para câncer de mama.')

st.write('A equipe recebeu inicialmente 4 Dataframes, os quais foram denominados como:') 
st.write('dfd: Dataframe de dados demográficos, nele estão contidas características do paciente, como: idade, educação, tratamento, sexo, gravidez, ultima informação, etc')
st.write('dfh: Dataframe de dados histopatológicos, nele estão contidas informações sobre a doença e os tecidos do indivíduo. Subtipo tumoral, Receptor de progesterona, Receptor de estrogênio  e grau histológico são apenas algumas das colunas que estão nessa tabela.')
st.write('dfpa: Dataframe de dados de peso e altura, possui informações como IMC,peso, altura, data, entre outras.')
st.write('dfrt: Dataframe de Registro tumoral, essa tabela possui características do tumor, tais quais: Estadio clínico, classificação TNM, combinações de tratamentos realizados no hospital, metástase, etc.')

st.write('Primeiramente, fizemos uma extensa análise exploratória inicial, observa-se os tipos de dados em cada coluna e foram plotados gráficos da quantidade de valores nulos em cada Dataframe.')

image = Image.open('image.png')
image1 = Image.open('image (1).png')
image2 = Image.open('image (2).png')
image3 = Image.open('image (3).png')
st.image(image)
st.image(image1)
st.image(image2)
st.image(image3)
