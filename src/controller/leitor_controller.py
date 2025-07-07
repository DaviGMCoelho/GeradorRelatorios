'''
Esse módulo é responsável por gerenciar a chamada dos métodos de manipução da planilha
'''
from src.service.leitor_service import LeitorService

class LeitorController:
    '''
    Esta classe irá conter os principais métodos para gerenciar a exibição dos dados
    Params:
        sheet_id : Número de identificação da planilha
        sheet_name : Nome da aba escolhida para utilização
    '''
    def __init__(self, sheet_id, sheet_name):
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name

    def show_sheet(self):
        '''
        Este método retorna a planilha inteira com todas as linhas
        '''
        leitor = LeitorService()
        data = leitor.get_sheet_data(self.sheet_id, self.sheet_name)
        return data
