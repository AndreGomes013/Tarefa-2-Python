from Tabela import Tabela

class TabelaBD(Tabela):
    def conta(self, coluna):
        # Inicialize um dicionário para contar o número de ocorrências de cada valor na coluna
        contador = {}

        # Encontre o índice da coluna no cabeçalho
        coluna_index = self.cabecalho.dados.index(coluna)

        # Percorra todas as linhas da tabela e conte as ocorrências
        for linha in self.dados:
            valor = linha.dados[coluna_index]
            if valor not in contador:
                contador[valor] = 0
            contador[valor] += 1

        # Crie uma tabela com os resultados
        resultado = Tabela()
        resultado.add_cabecalho([coluna, 'numero'])
        for valor, numero in contador.items():
            resultado.addLinha(Linha([valor, numero]))

        return resultado

    def ordena_por(self, coluna):
        # Encontre o índice da coluna no cabeçalho
        coluna_index = self.cabecalho.dados.index(coluna)

        # Ordene as linhas da tabela com base na coluna especificada
        self.dados.sort(key=lambda linha: linha.dados[coluna_index])

    def select(self, coluna, valor):
        # Encontre o índice da coluna no cabeçalho
        coluna_index = self.cabecalho.dados.index(coluna)

        # Filtrar as linhas da tabela onde a coluna especificada possui o valor desejado
        linhas_filtradas = [linha for linha in self.dados if linha.dados[coluna_index] == valor]

        # Crie uma nova tabela com as linhas filtradas
        resultado = Tabela()
        resultado.add_cabecalho(self.cabecalho.dados)
        for linha in linhas_filtradas:
            resultado.addLinha(Linha(linha.dados))

        return resultado
