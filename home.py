import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image



image = Image.open('higia.png')
col1, col2, col3 = st.columns(3)

with col2:
    st.image(image, width=200)

st.write('Nascido de uma parceira entre o Instituto de Tecnologia e Liderança (Inteli) e a Faculdade de Medicina da USP (FMUSP), o grupo Higia foi inspirado para seu nome na deusa grega da saúde ‘Higeia’ e tem como objetivo desenvolver soluções inovadoras para hospitais e clínicas, usando inteligência artificial para aprimorar a velocidade e precisão na prescrição de tratamentos para pacientes com câncer de mama.')
st.write('O objetivo é ajudar/auxiliar os médicos a tomar decisões mais rápidas e precisas, o que pode ser crucial para o sucesso do tratamento.')
st.write(' As soluções desenvolvidas pelo grupo incluem algoritmos de aprendizado de máquina que analisam dados de pacientes, incluindo histórico médico e resultados de laboratórios. Esses algoritmos podem ajudar os médicos a identificar padrões e fazer previsões precisas sobre o resultado do tratamento, o que pode levar a uma terapia mais eficaz e personalizada. Isso pode ajudar a reduzir erros médicos e melhorar a qualidade geral do cuidado com os pacientes')

st.markdown("<h1 style='text-align: center; color: Black;'>Projeto Agatha</h1>", unsafe_allow_html=True)

st.write('Com nossas soluções inovadoras e personalizadas, estamos ajudando a tornar o tratamento do câncer de mama mais eficiente e preciso. Com aplicações da inteligência artificial, o grupo está transformando a maneira como os médicos abordam o tratamento do câncer de mama, fornecendo melhores resultados e mais esperança para os pacientes e suas famílias.')

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("<h4 style='text-align: center; color: Black;'>Alunos</h4>", unsafe_allow_html=True)
    st.write("[Fabio Piemonte](https://www.linkedin.com/in/fabio-piemonte-823a65211/_)")
    st.write("[Marcelo Maia](https://www.linkedin.com/in/marcelo-maia-b90b03231/)")
    st.write("[Enya Oliveira]( https://www.linkedin.com/in/enya-oliveira-636566240/)")
    st.write("[Isabela Rocha](https://www.linkedin.com/in/isabela-amado-da-rocha-0314b42)")
    st.write("[Luis Miranda](https://www.linkedin.com/in/luis-miranda-137566139/)")
    st.write("[Thomaz Klifson](https://www.linkedin.com/in/thomaz-klifson-falcão-barboza-046490125/)")
    st.write("[Yago Araújo](https://www.linkedin.com/in/yago-araújo-do-vale-moreira-461816247/)")


with col5:
    st.markdown("<h4 style='text-align: center; color: Black;'>Instituições Parceiras</h4>", unsafe_allow_html=True)

with col6:
    st.markdown("<h4 style='text-align: center; color: Black;'>GitHub</h4>", unsafe_allow_html=True)
    st.write("[GitHub](https://github.com/2023M3T5-Inteli/grupo3)")
    