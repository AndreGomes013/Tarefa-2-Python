class Linha:
    def __init__(self):
        self.dados = []

    def append(self, x):
        if isinstance(x, list):
            self.dados.extend(x)
        else:
            self.dados.append(x)

    def __str__(self):
        numeros = ",".join(str(item) for item in self.dados)
        tamanho = len(self.dados)
        return f"{numeros}({tamanho})"

    def __len__(self):
        return len(self.dados)


aux = Linha()
# o parâmetro é uma lista
aux.append([1, 2, 3, 4, 3])
# o parâmetro não é uma lista
aux.append(2)

print(aux)
print("Comprimento:"+str(len(aux)))



