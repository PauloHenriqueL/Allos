import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from Terapeuta.service import TerapeutaService
from decano.service import DecanoService
from nucleo.service import NucleoService



def show_terapeutas():
    terapeuta_service = TerapeutaService()
    terapeuta = terapeuta_service.get_terapeuta()
    
    if terapeuta:
        st.write('Lista Terapeuta')
        terapeuta_df = pd.json_normalize(terapeuta)
        # Converte a lista de dicionários em um DataFrame
        # Exibe o DataFrame na tabela AgGrid
        AgGrid(
            data=terapeuta_df,
            reload_data=True,
            key='terapeuta_grid',    
        )
    else:
        st.warning('Nenhum terapeuta encontrado')

    st.title('Cadastrar novo Terapeuta')

    nome = st.text_input('Nome')
    usuario = st.text_input('Usuário')
    telefone = st.text_input('Telefone')
    email = st.text_input('Email')
    abordagem = st.text_input('Abordagem')

    decano_service = DecanoService()
    decanos = decano_service.get_decano()
    decano_names = {decano['nome']: decano['id'] for decano in decanos}
    selected_decano_name = st.selectbox('Decano', list(decano_names.keys()))

    nucleo_service = NucleoService()
    nucleos = nucleo_service.get_nucleo()
    nucleo_names = {nucleo['nome']: nucleo['id'] for nucleo in nucleos}
    selected_nucleo_name = st.selectbox('Nucleo', list(nucleo_names.keys()))

    if st.button('Cadastrar'):
        new_terapeuta = terapeuta_service.create_terapeuta(
            nome=nome,
            usuario=usuario,
            telefone=telefone,
            email=email,
            decano=decano_names[selected_decano_name],
            nucleo=nucleo_names[selected_nucleo_name],
            abordagem=abordagem,
        )
        if new_terapeuta:
            st.rerun()
        else:
            st.error('Verifique os campos')
