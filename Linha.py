class Linha:
    def __init__(self):
        self.dados = []

    def append(self, valor):
        if isinstance(valor, list):
            self.dados.extend(valor)
        else:
            self.dados.append(valor)

    def __str__(self):
        return str(self.dados)

    def __len__(self):
        return len(self.dados)
