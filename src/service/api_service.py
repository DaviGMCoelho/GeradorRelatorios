'''
Esse módulo é responsável pelas requisições da API
'''
from src.client.api_client import APIClient

class APIService:
    '''
    Essa classe gerencia todas as requisições a API
    '''
    def __init__(self, sample_id, sample_name):
        self.sample_id = sample_id
        self.sample_name = sample_name

    def get_trated_sample(self):
        '''
        Pega os dados da planilha
        '''
        client = APIClient()
        sample = client.get_sample_raw(self.sample_id, self.sample_name)
        return sample
