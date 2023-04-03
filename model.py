import streamlit as st
import pandas as pd
import numpy as np
import joblib


load_model = joblib.load('finalized_model.sav')
load_normalizacao = joblib.load('normalizacao.sav')

st.title('Agatha predictive model')


with st.form("my_form"):
    idade_primeiro_diagnostico = st.slider("Qual a idade no primeiro diagnóstico?", 0, 100, 25)

    radioterapia = st.selectbox(
            "Fez radioterapia",
            ("Sim", "Não")
        )   #1

    grupo_estadio_clinico = int(st.selectbox(
        'Qual o grupo do estadio clínico',
        ('0', '1', '2', '3', '4')))

    t_tnm = int(st.selectbox(
        'Qual o T do TNM',
        ('0', '1', '2', '3', '4')))

    n_tnm = int(st.selectbox(
        'Qual o N do TNM',
        ('0', '1', '2', '3')))

    subtipotumoral = int(st.selectbox(
        'Qual o subtipo_tumoral',
        ('1', '2', '3', '4', '5')))

    indice_h_receptorde_progesterona = st.slider("Qual o indice h do receptor deprogesterona?", 0, 300, 25)

    ki67_pct = st.slider("Qual o ki67_pct?", 1, 100, 25)

    receptor_estrogenio = st.selectbox(
            "Receptor Estrogênio",
            ("Sim", "Não")
        )  #1

    receptor_progesteronastrogenio = st.selectbox(
            "Receptor Progesterona",
            ("Sim", "Não")
        )#1

    receptor_progesterona_quantificacao_pct = st.slider("Qual o receptor_progesterona_quantificacao_pct?", 0, 100, 25)

    receptorde_estrogenio_quantificacao_pct = st.slider("Qual o receptorde_estrogenio_quantificacao_pct?", 0, 100, 25)

    ki67_maior14pct = st.selectbox(
            "ki67_maior14pct",
            ("Sim", "Não")
        )#1

    

   

   # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    x = [idade_primeiro_diagnostico, radioterapia, grupo_estadio_clinico, t_tnm, n_tnm, subtipotumoral, indice_h_receptorde_progesterona, ki67_pct,
        receptor_estrogenio, receptor_progesteronastrogenio, receptor_progesterona_quantificacao_pct,
        receptorde_estrogenio_quantificacao_pct, ki67_maior14pct]
    
    for i in range(0, len(x)):
            if type(x[i]) == str:
                if x[i] == 'Sim':
                    x[i] = float(1)
                else:
                    x[i] = float(0)

    
    x = np.array(x)
    x = x.reshape(1,-1)
    x = load_normalizacao.transform(x)

    if submitted:
        prediction = load_model.predict(x)
        if prediction == 1:
            st.write('Neoadjuvante')
        else:
            st.write('adjuvante')