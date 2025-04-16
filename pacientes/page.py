import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from pacientes.models import Paciente


def show_pacientes():
    st.write('Lista Pacientes')

    # Consulta os objetos do modelo pacientes
    pacientess = Paciente.objects.all().values()  # Retorna uma QuerySet como uma lista de dicionários

    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(pacientess)

    # Exibe o DataFrame na tabela AgGrid
    AgGrid(
        data=df,
        reload_data=True,
        key='pacientes_grid',
    )

    st.title('Cadastrar novo Paciente')
    name = st.text_input('Novo Paciente')
    if st.button('Cadastrar'):
        st.success(f'Paciente de "{name}" cadastrado com sucesso')
