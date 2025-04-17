import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from nucleo.service import NucleoService


def show_nucleo():
    nucleo_service = NucleoService()
    nucleos = nucleo_service.get_nucleo()
    
    if nucleos:
        st.write('Lista Nucleos')
        nucleo_df = pd.json_normalize(nucleos)
        # Converte a lista de dicionários em um DataFrame
        # Exibe o DataFrame na tabela AgGrid
        AgGrid(
            data=nucleo_df,
            reload_data=True,
            key='nucleo_grid',    
        )
    else:
        st.warning('Nenhum nucleo encontrado')

    st.title('Cadastrar novo Nucleo')
    nome = st.text_input('Nome')
    if st.button('Cadastrar'):
        new_nucleo = nucleo_service.create_nucleo(
            name=nome,
        )
        if new_nucleo:
            st.rerun()
        else:
            st.error('Verifique os campos')
