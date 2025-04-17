from pacientes.repository import PacienteRepository


class PacienteService:
    
    
    def __init__(self):
        self.pacientes_repository = PacienteRepository()
    
    def get_pacientes(self):
        return self.pacientes_repository.get_paciente()
    
    #Monta os dados para enviar para o repository
    def create_pacientes(self, nome, usuario, telefone, contapoio, valor, quantidade_de_sessoes, terapeuta):
        pacientes = dict(
            nome=nome,
            usuario=usuario,
            telefone=telefone,
            contapoio=contapoio,
            valor=valor,
            quantidade_de_sessoes=quantidade_de_sessoes,
            terapeuta=terapeuta,
        )
        return self.pacientes_repository.create_paciente(pacientes)
        #Envia pacientes para o repository
