class MvpUtil:
    #    def __init__(self, nome, idade):
    #
    #        self.nome = nome
    #
    #        self.idade = idade

    # Exibir Qtde de Linhas do Dataset
    @staticmethod
    def printQtdLinhasDataFrame(df):
        lQtd = df.shape[0]
        md(f'####{lQtd=}')
        return lQtd
    
    @staticmethod
    def teste(df):
        print('teste')