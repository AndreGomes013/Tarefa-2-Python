from Linha import Linha


class Tabela:
    def __init__(self):
        self.dados = []
        self.cabecalho = Linha()

    def add_cabecalho(self, valores):
        self.cabecalho.append(valores)

    def addLinha(self, valores):
        if len(valores) != len(self.cabecalho):
            print("tamanho da linha incompatível")
            return
        nova_linha = Linha()
        nova_linha.append(valores)
        self.dados.append(nova_linha)

    def __str__(self):
        result = [str(self.cabecalho)]
        result.append("-" * len(str(self.cabecalho)))
        for linha in self.dados:
            result.append(str(linha))
        return '\n'.join(result)




tab = Tabela()
tab.add_cabecalho(["Placa", "Ano", "Marca", "Modelo"])
carro = Linha()
carro.append(["ZBB1B11", 1998, "Ford", "Ka"])
tab.addLinha(carro)
carro = Linha()
carro.append(["BBB1B22", 2010, "Ford", "Fusion"])
tab.addLinha(carro)
carro = Linha()
carro.append(["DBB1B33", 2020, "Fiat", "Uno"])
tab.addLinha(carro)
carro = Linha()
carro.append(["CBB1B00", 2015, "Volks", "Gol"])
tab.addLinha(carro)

print(tab)

carro = Linha()
carro.append(["CBB1B00", 2015, "Volks", "Gol", "Teste"])
tab.addLinha(carro)

