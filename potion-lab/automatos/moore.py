class MooreFrankenstein:
    def __init__(self):
        self.estado = 'INICIO'
        self.partes = {
            'cabeca': 0,
            'tronco': 0,
            'braco': 0,
            'perna': 0
        }

    def _atualizar_estado(self):
        if self.partes['cabeca'] == 1 and \
           self.partes['tronco'] == 1 and \
           self.partes['braco'] == 2 and \
           self.partes['perna'] == 2:
            self.estado = 'COMPLETO'
        elif self.partes['tronco'] == 1:
            self.estado = 'MONTANDO'
        else:
            self.estado = 'INCOMPLETO'

    def adicionar_parte(self, parte):
        if self.estado == 'COMPLETO':
            print("🧟 Frankenstein já está completo!")
            return

        if parte not in self.partes:
            print("❌ Parte inválida!")
            return

        limite = 1 if parte in ['cabeca', 'tronco'] else 2
        if self.partes[parte] < limite:
            self.partes[parte] += 1
            print(f"✅ Parte adicionada: {parte}")
        else:
            print(f"⚠️ Já há {limite} {parte}(s).")

        self._atualizar_estado()
        print(self.saida_estado())

    def saida_estado(self):
        if self.estado == 'COMPLETO':
            return self._frankenstein_visual()
        elif self.estado == 'MONTANDO':
            return f"🔧 Montagem em progresso: {self.partes}"
        else:
            return f"🧩 Ainda incompleto: {self.partes}"

    def _frankenstein_visual(self):
        # Montagem final com emojis:
        return """
🧟 Frankenstein COMPLETO!
"""

