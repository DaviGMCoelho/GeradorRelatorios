import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class APIClient:
    '''
    Recebe os parâmetros necessários para a conexão com a API
    Params:
        scopes : Limitação de uso da API / Nível de acesso
        creds : Credenciais de acesso
        service : Serviço de utilização da API
    '''
    def __init__(self):
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.creds = None
        self.service = None

    def _create_service(self):
        service = build('sheets', 'v4', credentials=self.creds)
        return service

    def _conexao(self):
        '''
        Estabelece a conexão com a API, usando o arquivo onde é armazenado as credenciais de acesso
        Arquivo de credenciais é criado automaticamente pela primeira vez
        '''
        try:
            if os.path.exists('token.json'): # Verifica se o arquivo já existe
                self.creds = Credentials.from_authorized_user_file('token.json', self.scopes)
            # Se não tiver credenciais válidas, abre uma tela de confirmação da Google
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', self.scopes
                    )
                    self.creds = flow.run_local_server(port=0)
                # Salva as credencias para próxima vez que rodar
                with open('token.json', 'w', encoding='utf-8') as token:
                    token.write(self.creds.to_json())

            self.service = self._create_service() # Método para criar um serviço da API

        except HttpError as err:
            print(err)

    def get_sample_raw(self, sample_id, sample_name):
        '''
        Retorna todos os dados da planilha no momento.
        '''
        self._conexao()
        sheet = self.service.spreadsheets() # pylint: disable=maybe-no-member
        sample = (
            sheet.values()
            .get(
                spreadsheetId=sample_id,
                range=sample_name
            )
            .execute()
        ).get('values', [])

        return sample
