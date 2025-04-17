import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from decano.service import DecanoService


def show_decano():
    decano_service = DecanoService()
    decanos = decano_service.get_decano()
    
    if decanos:
        st.write('Lista Decanos')
        decano_df = pd.json_normalize(decanos)
        # Converte a lista de dicionários em um DataFrame
        # Exibe o DataFrame na tabela AgGrid
        AgGrid(
            data=decano_df,
            reload_data=True,
            key='decano_grid',    
        )
    else:
        st.warning('Nenhum decano encontrado')

    st.title('Cadastrar novo Decano')
    nome = st.text_input('Nome')
    email = st.text_input('Email')
    telefone = st.text_input('Telefone')
    if st.button('Cadastrar'):
        new_decano = decano_service.create_decano(
            nome=nome,
            email=email,
            telefone=telefone,
        )
        if new_decano:
            st.rerun()
        else:
            st.error('Verifique os campos')
