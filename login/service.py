import streamlit as st
from authentication.service import Auth


  # Usa o service de authentication para buscar um token e salvar no session_state
def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(  # Retorne um authtoken para esse username e password
        username=username,
        password=password,
    )
    if response.get('error'):
        st.error(f'Falha ao realizar login: {response.get("error")}')  # Se der erro devolva a mensagem de error
    else:
        st.session_state.token = response.get('access')  # Se der certo, salve o access que foi retornado em session_state
        st.rerun()