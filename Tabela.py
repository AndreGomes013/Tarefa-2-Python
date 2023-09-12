from Linha import Linha

class Tabela:
    def __init__(self):
        self.cabecalho = Linha()
        self.dados = []

    def add_cabecalho(self, valor):
        self.cabecalho = Linha()
        self.cabecalho.append(valor)

    def addLinha(self, linha):
        if len(linha) != len(self.cabecalho):
            print("Tamanhos incompatíveis")
        else:
            self.dados.append(linha)

    def __str__(self):
        result = str(self.cabecalho) + "\n" + "-" * (len(self.cabecalho) * 15) + "\n"
        for linha in self.dados:
            result += str(linha) + "\n"
        return result

    def ordena_por(self, valor):
        print(f"Ordenação por {valor}:")
        index = self.cabecalho.dados.index(valor)
        self.dados.sort(key=lambda x: x.dados[index])

    def ordena_por_ano(self):
        self.ordena_por("Ano")

    def ordena_por_modelo(self):
        self.ordena_por("Modelo")

    def ordena_por_placa(self):
        self.ordena_por("Placa")
