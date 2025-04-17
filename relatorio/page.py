import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from datetime import datetime
from relatorio.service import RelatorioService
from Terapeuta.service import TerapeutaService
from decano.service import DecanoService
from pacientes.service import PacienteService

def show_relatorio():
    st.write('Lista Relatorios')
    relatorio_service = RelatorioService()
    relatorios = relatorio_service.get_relatorio()
    
    if relatorios:
        st.write('Lista Relatorios')
        relatorio_df = pd.json_normalize(relatorios)
        relatorio_df = relatorio_df.drop(columns=['created_at','update_at'])
        AgGrid(
            data=relatorio_df,
            reload_data=True,
            key='relatorio_grid',    
        )
    else:
        st.warning('Nenhum relatorio encontrado')
    
    st.title('Cadastrar novo Relatorio')
    
    decano_service = DecanoService()
    decanos = decano_service.get_decano()
    decano_names = {decano['nome']: decano['id'] for decano in decanos}
    selected_decano_name = st.selectbox('Decano', list(decano_names.keys()))
    
    paciente_service = PacienteService()
    pacientes = paciente_service.get_pacientes()
    paciente_names = {paciente['nome']: paciente['id'] for paciente in pacientes}
    selected_paciente_name = st.selectbox('Paciente', list(paciente_names.keys()))
    
    terapeuta_service = TerapeutaService()
    terapeutas = terapeuta_service.get_terapeuta()
    terapeuta_names = {terapeuta['nome']: terapeuta['id'] for terapeuta in terapeutas}
    selected_terapeuta_name = st.selectbox('Terapeuta', list(terapeuta_names.keys()))
    
    data = st.date_input(
        label='Data',
        value=datetime.today(),
        format='DD/MM/YYYY',
    )
    
    choices_dropdown = ['Sim', 'Não', 'Não se aplica']
    sessao_1_realizado = st.radio(
        label='Sessão 1 foi realizada?',
        options=choices_dropdown,
    )
    sessao_1_pago = st.radio(
        label='Sessão 1 foi paga?',
        options=choices_dropdown,
    )
    sessao_2_realizado = st.radio(
        label='Sessão 2 foi realizada?',
        options=choices_dropdown,
    )
    sessao_2_pago = st.radio(
        label='Sessão 2 foi paga?',
        options=choices_dropdown,
    )
    sessao_3_realizado = st.radio(
        label='Sessão 3 foi realizada?',
        options=choices_dropdown,
    )
    sessao_3_pago = st.radio(
        label='Sessão 3 foi paga?',
        options=choices_dropdown,
    )
    sessao_4_realizado = st.radio(
        label='Sessão 4 foi realizada?',
        options=choices_dropdown,
    )
    sessao_4_pago = st.radio(
        label='Sessão 4 foi paga?',
        options=choices_dropdown,
    )
    if st.button('Cadastrar'):
        new_relatorio = relatorio_service.create_relatorio(
            decano=decano_names[selected_decano_name],
            paciente=paciente_names[selected_paciente_name],
            Terapeuta=terapeuta_names[selected_terapeuta_name], 
            data=data,
            sessao_1_realizado=sessao_1_realizado,
            sessao_1_pago=sessao_1_pago,
            sessao_2_realizado=sessao_2_realizado,
            sessao_2_pago=sessao_2_pago,
            sessao_3_realizado=sessao_3_realizado,
            sessao_3_pago=sessao_3_pago,
            sessao_4_realizado=sessao_4_realizado,
            sessao_4_pago=sessao_4_pago,
        )
        if new_relatorio:
            st.rerun()
        else:
            st.error('Verifique os campos')
