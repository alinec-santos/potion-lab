class MaquinaTuring:
    def __init__(self, palavra):
        self.fita = list(palavra) + ['_']  # Delimitador de fim
        self.estado = 'q0'
        self.posicao = 0

    def executar(self):
        while True:
            simbolo = self.fita[self.posicao]

            if self.estado == 'q0':
                if simbolo not in ['X', '_']:
                    self.simbolo_inicial = simbolo
                    self.fita[self.posicao] = 'X'
                    self.estado = 'direita'
                    self.posicao += 1
                elif simbolo == 'X' or simbolo == '_':
                    self.estado = 'aceita'
                    break
                else:
                    self.estado = 'rejeita'
                    break

            elif self.estado == 'direita':
                if self.fita[self.posicao] != '_':
                    self.posicao += 1
                else:
                    self.posicao -= 1
                    self.estado = 'verifica'

            elif self.estado == 'verifica':
                if self.fita[self.posicao] == self.simbolo_inicial:
                    self.fita[self.posicao] = 'X'
                    self.estado = 'volta_inicio'
                    self.posicao -= 1
                elif self.fita[self.posicao] == 'X':
                    self.estado = 'volta_inicio'
                    self.posicao -= 1
                else:
                    self.estado = 'rejeita'
                    break

            elif self.estado == 'volta_inicio':
                if self.fita[self.posicao] != 'X':
                    self.posicao -= 1
                else:
                    self.posicao += 1
                    self.estado = 'q0'
            else:
                break

        if self.estado == 'aceita':
            print("Palindromo!")
            return 'aceita'
        else:
            print("Não é um palindromo!")
            return 'rejeita'

