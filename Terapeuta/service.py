from Terapeuta.repository import TerapeutaRepository


class TerapeutaService:
    
    def __init__(self):
        self.terapeuta_repository = TerapeutaRepository()
    
    def get_terapeuta(self):
        return self.terapeuta_repository.get_terapeuta()
    
    #Monta os dados para enviar para o repository
    def create_terapeuta(self, nome, usuario, telefone, email, decano, nucleo, abordagem):
        terapeuta = dict(
            nome=nome,
            usuario=usuario,
            telefone=telefone,
            email=email,
            decano=decano,
            nucleo=nucleo,
            abordagem=abordagem,
        )
        return self.terapeuta_repository.create_terapeuta(terapeuta)
        #Envia terapeuta para o repository
