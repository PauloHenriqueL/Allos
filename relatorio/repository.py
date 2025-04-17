import requests
import streamlit as st
from login.service import logout


#  Faça um authetication jwt na url e me traga o access e o refresh
class RelatorioRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__relatorio_url = f'{self.__base_url}relatorio'
        self.__headers = {
            'Authorization' : f'Bearer {st.session_state.token}'
        }
    
    def get_relatorio(self):
        response = requests.get(
            self.__relatorio_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
             return logout()
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_relatorio(self, relatorio):
        response = requests.post(
            self.__relatorio_url,
            headers=self.__headers,
            data=relatorio,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')