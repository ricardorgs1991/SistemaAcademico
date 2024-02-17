"""
Objeto Classe, cria turmas com os estudantes
"""
import pandas as pd

class Classe:
    def __init__(self, estudantes):
        """
        Método construtor para o objeto Classe
        :param estudantes: Lista com todos os estudantes de uma classe
        """
        self.estudantes = estudantes

    def ler_arquivo(self):
        caminho_arquivo = (r"C:\Users\WIN\PycharmProjects\sistemaAcademico\Academico"
                           r"\Listadealunos.xlsx")
        tabela = pd.read_excel(caminho_arquivo)
        #Desenvolver (classe com estudantes)

