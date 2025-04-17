import requests
import streamlit as st
from login.service import logout


response = requests.get('http://localhost:8000/api/v1/decano', verify=False)
#  Faça um authetication jwt na url e me traga o access e o refresh
class DecanoRepository:
    
    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__decano_url = f'{self.__base_url}decano'
        self.__headers = {
            'Authorization' : f'Bearer {st.session_state.token}'
        }
    
    def get_decano(self):
        response = requests.get(
            self.__decano_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_decano(self, decano):
        response = requests.post(
            self.__decano_url,
            headers=self.__headers,
            data=decano,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
