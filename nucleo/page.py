import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from nucleo.models import Nucleo



def show_nucleo():
    st.write('Lista Nucleos')

    # Consulta os objetos do modelo nucleo
    nucleos = Nucleo.objects.all().values()  # Retorna uma QuerySet como uma lista de dicionários

    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(nucleos)

    # Exibe o DataFrame na tabela AgGrid
    AgGrid(
        data=df,
        reload_data=True,
        key='nucleo_grid',    
    )

    st.title('Cadastrar novo Nucleo')
    name = st.text_input('Novo Nucleo')
    if st.button('Cadastrar'):
        st.success(f'Nucleo de "{name}" cadastrado com sucesso')
