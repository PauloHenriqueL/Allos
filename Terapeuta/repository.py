import requests
import streamlit as st
from login.service import logout


class TerapeutaRepository:
    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__terapeuta_url = f'{self.__base_url}terapeuta'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.get("token", "")}'
        }

    def __handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            st.error("Sessão expirada. Faça login novamente.")
            return None
        st.error(f'Erro ao acessar a API. Status code: {response.status_code}')
        response.raise_for_status()

    def get_terapeuta(self):
        try:
            response = requests.get(
                self.__terapeuta_url,
                headers=self.__headers,
            )
            return self.__handle_response(response)
        except requests.RequestException as e:
            st.error(f"Erro de conexão: {e}")
            return None

    def create_terapeuta(self, terapeuta):
        required_fields = ["nome", "usuario", "telefone", "email", "abordagem"]
        missing_fields = [field for field in required_fields if not terapeuta.get(field)]

        if missing_fields:
            st.error(f"Os seguintes campos são obrigatórios: {', '.join(missing_fields)}")
            return None

        try:
            response = requests.post(
                self.__terapeuta_url,
                headers=self.__headers,
                json=terapeuta,  # Use `json` instead of `data` for JSON payloads
            )
            return self.__handle_response(response)
        except requests.RequestException as e:
            st.error(f"Erro de conexão: {e}")
            return None
