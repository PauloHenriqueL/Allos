from decano.repository import DecanoRepository


class DecanoService:
    
    
    def __init__(self):
        self.decano_repository = DecanoRepository()
    
    def get_decano(self):
        return self.decano_repository.get_decano()
    
    #Monta os dados para enviar para o repository
    def create_decano(self, nome, email, telefone):
        decano = dict(
            nome=nome,
            email=email,
            telefone=telefone,
        )
        return self.decano_repository.create_decano(decano)
        #Envia decano para o repository
