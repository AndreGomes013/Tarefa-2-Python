from Linha import Linha

class Tabela:
    def __init__(self, arquivo=None):
        self.cabecalho = Linha()
        self.dados = []

        if arquivo:
            self.loadFile(arquivo)

    def add_cabecalho(self, valor):
        self.cabecalho = Linha()
        self.cabecalho.append(valor)

    def addLinha(self, linha):
        if len(linha) != len(self.cabecalho):
            print("Tamanhos incompatíveis")
        else:
            self.dados.append(linha)

    def loadFile(self, arquivo):
        with open(arquivo, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    line = line.replace("', '", "','")  # Remove espaços entre as vírgulas
                    cabecalho = [val.strip('\'[]') for val in
                                 line.strip().split(',')]  # Remova os colchetes e as aspas7
                    self.add_cabecalho(cabecalho)
                else:
                    line = line.replace("', '", "','")  # Remove espaços entre as vírgulas
                    valores = [val.strip('\'[]') for val in line.strip().split(',')]  # Remova os colchetes e as aspas
                    self.addLinha(Linha(valores))

    def writeFile(self, arquivo):
        with open(arquivo, 'w') as file:
            file.write(str(self))

    def __str__(self):
        result = str(self.cabecalho) + "\n"
        for linha in self.dados:
            result += str(linha.dados) + "\n"
        return result

