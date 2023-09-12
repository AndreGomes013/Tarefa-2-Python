from Tabela import Tabela

class TabelaBD(Tabela):
    def __init__(self, arquivo=None):
        super().__init__()
        if arquivo:
            self.loadFile(arquivo)

    def conta(self, coluna, arquivo=None):
        if coluna not in self.cabecalho.dados:
            print(f"A coluna '{coluna}' não existe no cabeçalho.")
            return None

        coluna_index = self.cabecalho.dados.index(coluna)
        valores_coluna = [linha.dados[coluna_index] for linha in self.dados]

        contagem = {}
        for valor in valores_coluna:
            if valor in contagem:
                contagem[valor] += 1
            else:
                contagem[valor] = 1

        # Criar uma lista formatada a partir do dicionário
        lista_formatada = []
        lista_formatada.append("Partido, numero")

        for chave, valor in sorted(contagem.items()):
            lista_formatada.append(f"{chave}, {valor}\n")

        # Se um nome de arquivo for fornecido, escreva a tabela no arquivo
        if arquivo:
            with open(arquivo, 'w') as f:
                f.write('\n'.join(lista_formatada))

        return lista_formatada

    def __str__(self):
        # Inicializa uma lista para armazenar a saída formatada
        output = []

        # Adiciona o cabeçalho formatado à lista
        output.append("['Partido', 'numero']")
        output.append("----------------------")

        # Faz a contagem dos partidos
        result = self.conta("Partido")

        # Ordena os resultados alfabeticamente
        sorted_result = sorted(result.items())

        # Adiciona os resultados formatados à lista
        for partido, contagem in sorted_result:
            output.append([partido, contagem])

        # Retorna a saída como uma lista de listas
        return output