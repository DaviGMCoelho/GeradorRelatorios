'''
Esse módulo é responsável por gerenciar a chamada dos métodos de manipução da planilha
'''
from src.service.leitor_service import LeitorService

class LeitorController:
    '''
    Esta classe irá conter os principais métodos para gerenciar a exibição dos dados
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
