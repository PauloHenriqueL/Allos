import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from relatorio.models import Relatorio


def show_relatorio():
    st.write('Lista Relatorios')

    # Consulta os objetos do modelo Relatorio
    relatorios = Relatorio.objects.all().values()  # Retorna uma QuerySet como uma lista de dicionários

    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(relatorios)

    # Exibe o DataFrame na tabela AgGrid
    AgGrid(
        data=df,
        reload_data=True,
        key='relatorio_grid',
    )

    st.title('Cadastrar novo Relatorio')
    name = st.text_input('Novo Relatorio')
    if st.button('Cadastrar'):
        st.success(f'Relatorio de "{name}" cadastrado com sucesso')
