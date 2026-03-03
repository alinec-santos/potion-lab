class APD:
    def __init__(self, caminho_arquivo):
        self.estados = set()
        self.estado_inicial = None
        self.estado_atual = None
        self.estado_final = None
        self.simbolos_pilha = set()
        self.alfabeto = set()
        self.transicoes = {}  # chave: (estado, simbolo_entrada, topo_pilha), valor: (novo_estado, nova_pilha)
        self.pilha = []
        self._carregar_arquivo(caminho_arquivo)

    def _carregar_arquivo(self, caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip() and not linha.startswith('#')]

        secao_transicoes = False
        for linha in linhas:
            if linha.startswith('Q:'):
                self.estados = set(linha[2:].strip().split())
            elif linha.startswith('I:'):
                self.estado_inicial = linha[2:].strip()
                self.estado_atual = self.estado_inicial
            elif linha.startswith('F:'):
                self.estado_final = linha[2:].strip()
            elif linha.startswith('P:'):
                self.simbolos_pilha = set(linha[2:].strip().split())
            elif linha.startswith('Alfabeto:'):
                self.alfabeto = set(linha[len('Alfabeto:'):].strip().split())
            elif linha == '---':
                break
            elif '->' in linha:
                esquerda, direita = linha.split('->')
                esquerda = esquerda.strip()
                direita = direita.strip()
                estado, simbolo, topo = [x.strip() for x in esquerda.split(',')]
                novo_estado, novo_topo = [x.strip() for x in direita.split(',')]
                self.transicoes[(estado, simbolo, topo)] = (novo_estado, novo_topo)

        # Símbolo inicial da pilha
        self.pilha.append('Z0')

       # print("Transições carregadas:")
        #for k, v in self.transicoes.items():
            #print(f"{k} -> {v}")

    def transicionar(self, simbolo):
        topo = self.pilha[-1] if self.pilha else 'Z0'
        chave = (self.estado_atual, simbolo, topo)

        if chave not in self.transicoes:
            print(f"Transição inválida para ({self.estado_atual}, {simbolo}, {topo})")
            return False

        novo_estado, nova_pilha = self.transicoes[chave]
        print(f"Transição: ({self.estado_atual}, {simbolo}, {topo}) -> ({novo_estado}, {nova_pilha})")
        self.estado_atual = novo_estado

        if nova_pilha == 'ε':
            if self.pilha:
                self.pilha.pop()
        else:
            self.pilha.append(nova_pilha)

        return True

    def executar(self):
        print("\nIniciando simulação do APD...\n")
        while True:
            simbolo = input("Insira o próximo ingrediente (ou 'fim' para encerrar): ").strip()
            if simbolo == 'fim':
                # Processar transições epsilon automaticamente até o fim possível
                while True:
                    topo = self.pilha[-1] if self.pilha else 'Z0'
                    chave_epsilon = (self.estado_atual, 'ε', topo)
                    if chave_epsilon in self.transicoes:
                        novo_estado, nova_pilha = self.transicoes[chave_epsilon]
                        print(f"Transição epsilon automática: ({self.estado_atual}, ε, {topo}) -> ({novo_estado}, {nova_pilha})")
                        self.estado_atual = novo_estado
                        if nova_pilha == 'ε':
                            self.pilha.pop()
                        else:
                            self.pilha.append(nova_pilha)
                    else:
                        break
                break

            if simbolo not in self.alfabeto:
                print("Ingrediente inválido!")
                continue
            if not self.transicionar(simbolo):
                print("Mistura falhou. Reações instáveis.")
                return

        if self.estado_atual == self.estado_final and (self.pilha[-1] == 'Z0' or len(self.pilha) == 0):
            print("\n✅ Poção criada com sucesso!")
        else:
            print("\n❌ Poção incompleta ou instável.")
