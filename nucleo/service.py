from nucleo.repository import NucleoRepository


class NucleoService:
    
    
    def __init__(self):
        self.nucleo_repository = NucleoRepository()
    
    def get_nucleo(self):
        return self.nucleo_repository.get_nucleo()
    
    #Monta os dados para enviar para o repository
    def create_nucleo(self, nome):
        nucleo = dict(
            nome=nome,
        )
        return self.nucleo_repository.create_nucleo(nucleo)
        #Envia nucleo para o repository
