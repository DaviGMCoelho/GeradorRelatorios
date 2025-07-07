'''
Aqui será o módulo responsável pelo gerenciamento do leitor
'''
from src.service.api_service import APIService

class LeitorService:
    '''
    Classe criada para a leitura / captura das planilhas do google sheets
    '''
    def get_sheet_data(self, sheet_id, sheet_name):
        '''
        Método de leitura dos dados da planilha selecionada, retorna todas as linhas da planilha
        '''
        sheet = APIService(sheet_id, sheet_name)
        data = sheet.get_trated_sample()
        return data

if __name__ == '__main__':
    ...
