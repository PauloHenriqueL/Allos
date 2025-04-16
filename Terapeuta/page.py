import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from Terapeuta.models import Terapeuta


def show_terapeutas():
    st.write('Lista Terapeutas')

    # Consulta os objetos do modelo Terapeutas
    Terapeutas = Terapeuta.objects.all().values()  # Retorna uma QuerySet como uma lista de dicionários

    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(Terapeutas)

    # Exibe o DataFrame na tabela AgGrid
    AgGrid(
        data=df,
        reload_data=True,
        key='terapeuta_grid',
    )

    st.title('Cadastrar novo Terapeuta')
    name = st.text_input('Novo Terapeuta')
    if st.button('Cadastrar'):
        st.success(f'Terapeuta de "{name}" cadastrado com sucesso')
