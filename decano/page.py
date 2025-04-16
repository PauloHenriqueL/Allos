import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from decano.models import Decano



def show_decano():
    st.write('Lista Decanos')

    # Consulta os objetos do modelo decano
    decanos = Decano.objects.all().values()  # Retorna uma QuerySet como uma lista de dicionários

    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(decanos)

    # Exibe o DataFrame na tabela AgGrid
    AgGrid(
        data=df,
        reload_data=True,
        key='decano_grid',    
    )

    st.title('Cadastrar novo Decano')
    name = st.text_input('Novo Decano')
    if st.button('Cadastrar'):
        st.success(f'Decano de "{name}" cadastrado com sucesso')
