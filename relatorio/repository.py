import requests
import streamlit as st
from login.service import logout


class RelatorioRepository:
    BASE_URL = 'http://localhost:8000/api/v1/'
    STATUS_OK = 200
    STATUS_CREATED = 201
    STATUS_UNAUTHORIZED = 401

    def __init__(self):
        self.__relatorio_url = f'{self.BASE_URL}relatorio'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def __handle_response(self, response):
        if response.status_code == self.STATUS_OK or response.status_code == self.STATUS_CREATED:
            return response.json()
        if response.status_code == self.STATUS_UNAUTHORIZED:
            logout()
            return None
        response.raise_for_status()

    def get_relatorio(self):
        response = requests.get(self.__relatorio_url, headers=self.__headers)
        return self.__handle_response(response)

    def create_relatorio(self, relatorio):
        response = requests.post(self.__relatorio_url, headers=self.__headers, json=relatorio)
        return self.__handle_response(response)

    def get_relatorio_stats(self):
        stats_url = f'{self.__relatorio_url}stats/'
        response = requests.get(stats_url, headers=self.__headers)
        return self.__handle_response(response)
