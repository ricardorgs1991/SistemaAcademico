class Estudante:
    """
    Cria a variavel estudante para o sistema acadêmico
    """
    def __init__(self, num, nome, av_tri1, av_tri2, av_tri3):
        """
        Método construtor para a variável estudante
        :param num: Número de chamada do estudante
        :param nome: Nome do estudante
        :param av_tri1: Lista com as notas das avaliações do 1ºtrimestre
        :param av_tri2: Lista com as notas das avaliações do 2ºtrimestre
        :param av_tri3: Lista com as notas das avaliações do 3ºtrimestre
        :param media_final: Média final do estudante, de acordo com os trimestres
        """
        self.num = num
        self.nome = nome
        self.__av_tri1 = av_tri1
        self.__av_tri2 = av_tri2
        self.__av_tri3 = av_tri3
        self.__media_final = self.media_anual(av_tri1, av_tri2, av_tri3)

    def __media_anual(self, av_tri1, av_tri2, av_tri3):
        """
        Método privado da classe, para calcular a média final
        :param av_tri1: Lista com as notas das avaliações do 1ºtrimestre
        :param av_tri2: Lista com as notas das avaliações do 2ºtrimestre
        :param av_tri3: Lista com as notas das avaliações do 3ºtrimestre
        :return: Média final do estudante (Média aritmética simples)
        """
        media = (sum(av_tri1) + sum(av_tri2) + sum(av_tri3))/3
        return media

