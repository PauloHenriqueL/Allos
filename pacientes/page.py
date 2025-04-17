import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from pacientes.service import PacienteService
from Terapeuta.service import TerapeutaService


def show_pacientes():
    pacientes_service = PacienteService()
    pacientes = pacientes_service.get_pacientes()
    
    if pacientes:
        st.write('Lista Pacientes')
        pacientes_df = pd.json_normalize(pacientes)
        # Converte a lista de dicionários em um DataFrame
        # Exibe o DataFrame na tabela AgGrid
        AgGrid(
            data=pacientes_df,
            reload_data=True,
            key='pacientes_grid',    
        )
    else:
        st.warning('Nenhum pacientes encontrado')

    st.title('Cadastrar novo Paciente')
    nome = st.text_input('Nome')
    usuario = st.text_input('Usuario')
    telefone = st.text_input('Telefone')
    contapoio = st.text_input('Contato de Apoio')
    valor = st.text_input('Preço por Sessão')
    
    qtsessoes_dropdown = [1, 2, 3, 4]
    quantidade_de_sessoes = st.selectbox(
        label='Quantidade de sessões',
        options=qtsessoes_dropdown,
    )
    
    terapeuta_service = TerapeutaService()
    terapeutas = terapeuta_service.get_terapeuta()
    terapeuta_names = {terapeuta['nome']: terapeuta['id'] for terapeuta in terapeutas}
    selected_terapeuta_name = st.selectbox('Terapeuta', list(terapeuta_names.keys()))

    if st.button('Cadastrar'):
        new_pacientes = pacientes_service.create_pacientes(
            nome=nome,
            usuario=usuario,
            telefone=telefone,
            contapoio=contapoio,
            valor=valor,
            quantidade_de_sessoes=quantidade_de_sessoes,
            terapeuta=terapeuta_names[selected_terapeuta_name],
        )
        if new_pacientes:
            st.rerun()
        else:
            st.error('Verifique os campos')
