import streamlit as st
import os
import django
# Configurando o Django para usar o arquivo de configurações correto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')  # Certifique-se de que 'app.settings' está correto
django.setup()
# Importando as páginas
from decano.page import show_decano
from pacientes.page import show_pacientes
from Terapeuta.page import show_terapeutas
from home.page import show_home
from login.page import show_login
from nucleo.page import show_nucleo
from relatorio.page import show_relatorio

def main():  # Organizando o código para deixar ele facil de entender
    
    if 'token' not in st.session_state:
        show_login()
    else:    
        st.title('ALLOS')

        menu_option = st.sidebar.selectbox(  # Criando sidebarselecetbox
            'MENU',
            ['Início', 'Relatório Mensal', 'Pacientes', 'Decanos', 'Terapeutas', 'Nucleo']
        )

        if menu_option == 'Início':  # Definindo caminho das opções do sidebar
            show_home()

        if menu_option == 'Relatório Mensal':
            show_relatorio()

        if menu_option == 'Pacientes':
            show_pacientes()

        if menu_option == 'Decanos':
            show_decano()

        if menu_option == 'Terapeutas':
            show_terapeutas()

        if menu_option == 'Nucleo':
            show_nucleo()

if __name__ == '__main__':
    main()
