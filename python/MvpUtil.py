class MvpUtil:

#    def __init__(self, nome, idade):
#
#        self.nome = nome
#
#        self.idade = idade

    # Exibir Qtde de Linhas do Dataset
    def printQtdLinhasDataFrame(df):
    @staticmethod
        
        lQtd = df.shape[0]
        md(f'####{lQtd=}')
        return lQtd