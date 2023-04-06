import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image, ImageDraw, ImageFont



image = Image.open('A G A T H A.png')

col1, col2, col3 = st.columns(3)


with col2:
    st.image(image)


st.markdown("<h2 style='text-align: center; color: Black;'>Modelo Preditivo</h2>", unsafe_allow_html=True)

load_model = joblib.load('modelo_stacking_clf.sav')
load_normalizacao = joblib.load('normalizacao.sav')


tab1, tab2 = st.tabs(["Predição única", "Predição em massa"])

prediction_f = 0

df = 0


with tab1:
#Forms
    with st.form("my_form"):
        idade_primeiro_diagnostico = st.slider("Qual a idade no primeiro diagnóstico?", 0, 100, 25)

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
        
        submitted = st.form_submit_button("Calcular")

        x = [idade_primeiro_diagnostico, grupo_estadio_clinico, t_tnm, n_tnm, subtipotumoral, indice_h_receptorde_progesterona, ki67_pct,
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
                st.markdown("<h3 style='text-align: center; color: Black;'>Adjuvante</h3>", unsafe_allow_html=True)
                prediction_f = 'Adjuvante'
            else:
                st.markdown("<h3 style='text-align: center; color: Black;'>Neoadjuvante</h3>", unsafe_allow_html=True)
                prediction_f = 'Neoadjuvante'
            
            x = [idade_primeiro_diagnostico, grupo_estadio_clinico, t_tnm, n_tnm, subtipotumoral, indice_h_receptorde_progesterona, ki67_pct,
            receptor_estrogenio, receptor_progesteronastrogenio, receptor_progesterona_quantificacao_pct,
            receptorde_estrogenio_quantificacao_pct, ki67_maior14pct, prediction_f]


            df = pd.DataFrame(np.array([x]), columns = ['idade_primeiro_diagnostico', 'grupo_estadio_clinico',
                'classificacao_tnm_clinico_t', 'classificacao_tnm_clinico_n',
                'subtipo_tumoral', 'indice_h_receptorde_progesterona', 'ki67_pct',
                'receptor_estrogenio', 'receptor_progesterona',
                'receptor_progesterona_quantificacao_pct',
                'receptorde_estrogenio_quantificacao_pct', 'ki67_maior14pct', 'tratamento'])


            #PIL

            #carregando a fonte utilizada
            font_normal = ImageFont.truetype("Montserrat-SemiBold.ttf", 36)
            for index, row in df.head(1).iterrows():
                if row['tratamento'] == 'Neoadjuvante': #Neoadjuvante
                    im = Image.open('tratamento_neoadj.png')
                    im = im.convert('RGB')
                elif row['tratamento'] == 'Adjuvante': #adjuvante
                    im = Image.open('tratamento_adj.png')
                    im = im.convert('RGB')

                preenchimento = ImageDraw.Draw(im)
            #abaixo queremos preencher com estádio Clínico do paciente
                if row['grupo_estadio_clinico'] == '0':
                    preenchimento.text((950 , 717), "0", font=font_normal, fill=(20,29,55))
                elif row['grupo_estadio_clinico'] == '1':
                    preenchimento.text((950 , 717), "I", font=font_normal, fill=(20,29,55))
                elif row['grupo_estadio_clinico'] == '2':
                    preenchimento.text((950 , 717), "II", font=font_normal, fill=(20,29,55))
                elif row['grupo_estadio_clinico'] == '3':
                    preenchimento.text((950 , 717), "III", font=font_normal, fill=(20,29,55))
                elif row['grupo_estadio_clinico'] == '4':
                    preenchimento.text((950 , 717), "IV", font=font_normal, fill=(20,29,55))
            #abaixo queremos preencher com subtipo tumoral do paciente
                if row['subtipo_tumoral'] == '1':
                    preenchimento.text((1425, 716), 'Luminal A', font=font_normal, fill=(20,29,55))
                elif row['subtipo_tumoral'] == '2':
                    preenchimento.text((1425, 716), 'Luminal B', font=font_normal, fill=(20,29,55))
                elif row['subtipo_tumoral'] == '3':
                    preenchimento.text((1425, 716), 'HER-2', font=font_normal, fill=(20,29,55))
                elif row['subtipo_tumoral'] == '4':
                    preenchimento.text((1425, 716), 'Triplo negativo', font=font_normal, fill=(20,29,55))
                elif row['subtipo_tumoral'] == '5':
                    preenchimento.text((1425, 716), 'Her-2 e Luminal B', font=font_normal, fill=(20,29,55))
                
                nova_largura = 1024
                nova_altura = 800
                im = im.resize((nova_largura,nova_altura))
                im.save('prescricao.png')
            
                image = Image.open('prescricao.png')

                st.image(image)
    

with tab2:
    big_df = 0

    uploaded_file = st.file_uploader("Escolha um arquivo .csv")
    if uploaded_file is not None:

        big_df = pd.read_csv(uploaded_file)

        big_df_normalized = load_normalizacao.transform(big_df)

        big_df_prediction = load_model.predict(big_df_normalized)

        big_df['tratamento'] = big_df_prediction

        def tratamento_to_name(row):
            if row['tratamento'] == 1:
                row['tratamento'] = 'Adjuvante'
            else:
                row['tratamento'] = 'Neoadjuvante'
            
            return row

        big_df = big_df.apply(tratamento_to_name, axis=1)

        big_df

        @st.cache_data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(big_df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )
    
