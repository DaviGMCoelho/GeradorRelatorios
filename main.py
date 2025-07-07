'''
Módulo principal do programa
'''
from src.controller.leitor_controller import LeitorController

class Main:
    '''
    Classe responsável por gerenciar a inicialização do sistema
    '''
    def init(self):
        '''
        Método contendo a lógica de incialização do sistema
        '''
        leitor = LeitorController('insira o id da planilha aqui', 'insira a aba que deseja')
        data = leitor.show_sheet()
        print(data)

main = Main()
main.init()
