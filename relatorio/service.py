from relatorio.repository import RelatorioRepository


class RelatorioService:
    
    
    def __init__(self):
        self.relatorio_repository = RelatorioRepository()
    
    def get_relatorio(self):
        return self.relatorio_repository.get_relatorio()
    
    #Monta os dados para enviar para o repository
    def create_relatorio(self, decano, paciente, Terapeuta, data, sessao_1_realizado, sessao_1_pago, sessao_2_realizado, sessao_2_pago, sessao_3_realizado, sessao_3_pago, sessao_4_realizado, sessao_4_pago,):
        relatorio = dict(
            decano=decano,
            paciente=paciente,
            Terapeuta=Terapeuta, 
            data=data,
            sessao_1_realizado=sessao_1_realizado,
            sessao_1_pago=sessao_1_pago,
            sessao_2_realizado=sessao_2_realizado,
            sessao_2_pago=sessao_2_pago,
            sessao_3_realizado=sessao_3_realizado,
            sessao_3_pago=sessao_3_pago,
            sessao_4_realizado=sessao_4_realizado,
            sessao_4_pago=sessao_4_pago,
        )
        return self.relatorio_repository.create_relatorio(relatorio)
        #Envia relatorio para o repository
