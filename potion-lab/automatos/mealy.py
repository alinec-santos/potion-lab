class MealyPocao:
    def __init__(self):
        self.estado = 'normal'  # estados possíveis: normal, congelada, fervendo
        self.transicoes = {
            ('normal', 'gelo'): ('congelada', '\nA poção congelou! 🧊'),
            ('normal', 'fogo'): ('fervendo', '\nA poção está fervendo! 🔥'),
            ('normal', 'agua'): ('normal', '\nÁgua adicionada, poção continua normal. 💧'),
            ('normal', 'po_magico'): ('normal', '\nPó mágico espalhado, poção brilha! ✨'),
            ('normal', 'ervas'): ('normal', '\nErvas adicionadas, aroma agradável! 🌿'),

            ('congelada', 'fogo'): ('normal', '\nA poção descongelou! 🔥❄️'),
            ('congelada', 'gelo'): ('congelada', '\nMais gelo adicionado, continua congelada. 🧊'),
            ('congelada', 'agua'): ('congelada', '\nÁgua fria adicionada, poção ainda congelada. ❄️💧'),
            ('congelada', 'po_magico'): ('congelada', '\nPó mágico não teve efeito no gelo. ❄️✨'),
            ('congelada', 'ervas'): ('congelada', '\nErvas congeladas dentro da poção. ❄️🌿'),

            ('fervendo', 'gelo'): ('normal', '\nA poção esfria e para de ferver. 🧊🔥'),
            ('fervendo', 'fogo'): ('fervendo', '\nFogo intensificado, poção mais quente! 🔥🔥'),
            ('fervendo', 'agua'): ('fervendo', '\nÁgua quente adicionada, mantém fervura. 🔥💧'),
            ('fervendo', 'po_magico'): ('fervendo', '\nPó mágico potencializa a fervura! ✨🔥'),
            ('fervendo', 'ervas'): ('fervendo', '\nErvas vaporizadas pela fervura! 🌿🔥'),
        }
        self.ingredientes = ['gelo', 'fogo', 'agua', 'po_magico', 'ervas']

    def processar_ingrediente(self, ingrediente):
        chave = (self.estado, ingrediente)
        if chave in self.transicoes:
            novo_estado, saida = self.transicoes[chave]
            self.estado = novo_estado
            return saida
        else:
            return "Ingrediente desconhecido ou ação inválida."

    def processar(self, ingrediente):
            chave = (self.estado, ingrediente)
            if chave in self.transicoes:
                novo_estado, resposta = self.transicoes[chave]
                self.estado = novo_estado
                return resposta
            else:
                return "❌ Ingrediente não teve efeito nesse estado."

    def iniciar_interacao(self):
        print("Bem-vindo ao Misturador de Poções Mealy!")
        print("Estado inicial da poção:", self.estado)
        print("Ingredientes disponíveis:")
        for ingr in self.ingredientes:
            print(f"- {ingr}")

        while True:
            ingrediente = input("\nDigite o ingrediente a adicionar (ou 'sair' para encerrar): ").strip().lower()
            if ingrediente == 'sair':
                print("Finalizando mistura. Estado final da poção:", self.estado)
                break
            elif ingrediente not in self.ingredientes:
                print("Ingrediente inválido. Por favor, escolha um da lista.")
                continue
            resposta = self.processar_ingrediente(ingrediente)
            print(resposta)
            print(f"Estado atual da poção: {self.estado}")

