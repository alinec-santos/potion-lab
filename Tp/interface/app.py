import tkinter as tk
from tkinter import simpledialog, messagebox
from automatos.afd import AFD
from automatos.apd import APD
from automatos.moore import MooreFrankenstein
from automatos.turing import MaquinaTuring
from automatos.mealy import MealyPocao

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Laboratório de Autômatos Mágicos ✨")
        self.root.geometry("900x700")
        self.root.config(bg="#f5f3ff")

        # Título
        self.title_label = tk.Label(
            root,
            text="🔮 Bem-vindo ao Laboratório de Poções Automatizadas!",
            font=("Garamond", 20, "bold"),
            fg="#4b0082",
            bg="#f5f3ff"
        )
        self.title_label.pack(pady=20)

        # Frame dos botões
        self.button_frame = tk.Frame(root, bg="#f5f3ff")
        self.button_frame.pack(pady=10)

        estilo_botao = {
            "font": ("Garamond", 12),
            "width": 25,
            "bg": "#dcd0ff",
            "activebackground": "#c6b4f0"
        }

        self.afd_button = tk.Button(self.button_frame, text="🧪 Montar Poção (AFD)", command=self.executar_afd, **estilo_botao)
        self.afd_button.grid(row=0, column=0, padx=5, pady=5)

        self.apd_button = tk.Button(self.button_frame, text="📚 Montar Poção (APD)", command=self.executar_apd, **estilo_botao)
        self.apd_button.grid(row=0, column=1, padx=5, pady=5)

        self.frank_button = tk.Button(self.button_frame, text="🧟 Montar Frankenstein (Moore)", command=self.executar_frankenstein, **estilo_botao)
        self.frank_button.grid(row=0, column=2, padx=5, pady=5)

        self.turing_button = tk.Button(self.button_frame, text="🔁 Validar Palíndromo (Turing)", command=self.executar_turing, **estilo_botao)
        self.turing_button.grid(row=1, column=0, padx=5, pady=5)

        self.mealy_button = tk.Button(self.button_frame, text="🌡️ Misturar Poção (Mealy)", command=self.iniciar_mealy, **estilo_botao)
        self.mealy_button.grid(row=1, column=1, padx=5, pady=5)
         # Botão para limpar
        self.clear_button = tk.Button(self.button_frame, text="🧹 Limpar Interface", command=self.limpar_interface, **estilo_botao)
        self.clear_button.grid(row=1, column=2, padx=5, pady=5)

        # Área de saída
        self.text_output = tk.Text(root, height=25, width=100, font=("Consolas", 10), bg="#fff8fc")
        self.text_output.pack(pady=20)
        self.imagem_frankenstein = None  

        # Estado para Mealy
        self.mealy = None
        self.botoes_ingredientes = []

    def limpar_interface(self):
        """Limpa toda a interface e remove visualizações"""
        # Limpar texto
        self.text_output.delete('1.0', tk.END)
        
        # Remover botões de ingredientes do Mealy
        for btn in self.botoes_ingredientes:
            btn.destroy()
        self.botoes_ingredientes.clear()
        
        # Resetar Mealy
        self.mealy = None
        
        self.text_output.insert(tk.END, "🧹 Interface limpa! Pronto para nova operação.\n")
    def executar_afd(self):
        self.text_output.delete('1.0', tk.END)
        afd = AFD("automatos/entradas/IngredientesAfd.txt")
        afd.resetar()
        self.text_output.insert(tk.END, "🧪 Início da produção de poção (AFD)!\n")
        ingredientes = ["agua", "petala", "oleo", "po", "raiz", "cristal"]
        self.text_output.insert(tk.END, "📜 Ingredientes disponíveis: " + ", ".join(ingredientes) + "\n\n")

        while True:
            simbolo = simpledialog.askstring("AFD", "Insira o símbolo do próximo ingrediente:")
            if not simbolo:
                break
            self.text_output.insert(tk.END, f"🔹 Ingrediente adicionado: {simbolo}\n")
            afd.transitar(simbolo)
            self.text_output.insert(tk.END, f"Estado atual: {afd.estado_atual}\n")

            if afd.estado_atual == afd.estado_erro:
                break

            continuar = messagebox.askyesno("Continuar?", "Deseja inserir mais um ingrediente?")
            if not continuar:
                break

        if afd.estado_atual == afd.estado_final:
            self.text_output.insert(tk.END, "\n✅ Poção criada com sucesso!\n")
        else:
            self.text_output.insert(tk.END, "\n❌ Erro na mistura.\n")

    def executar_apd(self):
        self.text_output.delete('1.0', tk.END)
        apd = APD("automatos/entradas/IngredientesApd.txt")
        self.text_output.insert(tk.END, "🧪 Início da produção de poção (APD)!\n")
        
        ingredientes = ["agua", "petala", "oleo", "po", "raiz", "cristal"]
        self.text_output.insert(tk.END, "📜 Ingredientes disponíveis: " + ", ".join(ingredientes) + "\n\n")

        while True:
            simbolo = simpledialog.askstring("APD", "Insira o símbolo do próximo ingrediente:")
            if not simbolo:
                break

            self.text_output.insert(tk.END, f"🔹 Ingrediente adicionado: {simbolo}\n")

            if simbolo not in apd.alfabeto:
                self.text_output.insert(tk.END, "⚠️ Ingrediente inválido!\n")
                continue

            topo = apd.pilha[-1] if apd.pilha else 'Z0'
            chave = (apd.estado_atual, simbolo, topo)
            
            if chave in apd.transicoes:
                prox_estado, prox_pilha = apd.transicoes[chave]
                self.text_output.insert(
                    tk.END,
                    f"🔄 Transição: ({apd.estado_atual}, {simbolo}, {topo}) → ({prox_estado}, {prox_pilha})\n"
                )
                
                # Executa a transição
                apd.estado_atual = prox_estado
                if prox_pilha == 'ε':
                    apd.pilha.pop()
                else:
                    apd.pilha.append(prox_pilha)
            else:
                self.text_output.insert(tk.END, f"❌ Sem transição para ({apd.estado_atual}, {simbolo}, {topo})\n")
                apd.estado_atual = 'erro'
                break

            continuar = messagebox.askyesno("Continuar?", "Deseja inserir mais um ingrediente?")
            if not continuar:
                # Processar transições epsilon automaticamente ao encerrar
                while True:
                    if not apd.pilha:
                        break
                        
                    topo = apd.pilha[-1]
                    chave_epsilon = (apd.estado_atual, 'ε', topo)
                    
                    if chave_epsilon in apd.transicoes:
                        novo_estado, nova_pilha = apd.transicoes[chave_epsilon]
                        self.text_output.insert(tk.END, f"🔄 Transição ε: ({apd.estado_atual}, ε, {topo}) → ({novo_estado}, {nova_pilha})\n")
                        apd.estado_atual = novo_estado
                        if nova_pilha == 'ε':
                            apd.pilha.pop()
                        else:
                            apd.pilha.append(nova_pilha)
                    else:
                        break
                break

        # Processar transições epsilon finais
        while apd.estado_atual == apd.estado_final and apd.pilha:
            topo = apd.pilha[-1]
            chave_epsilon = (apd.estado_atual, 'ε', topo)
            
            if chave_epsilon in apd.transicoes:
                novo_estado, nova_pilha = apd.transicoes[chave_epsilon]
                self.text_output.insert(tk.END, f"🔄 Transição ε final: ({apd.estado_atual}, ε, {topo}) → ({novo_estado}, {nova_pilha})\n")
                apd.estado_atual = novo_estado
                if nova_pilha == 'ε':
                    apd.pilha.pop()
                else:
                    apd.pilha.append(nova_pilha)
            else:
                break

        # Verificação final corrigida
        pilha_aceitavel = (not apd.pilha) or (apd.pilha == ['Z0'])
        
        if apd.estado_atual == apd.estado_final and pilha_aceitavel:
            self.text_output.insert(tk.END, "\n✅ Poção criada com sucesso!\n")
            self.text_output.insert(tk.END, f"Estado final: {apd.estado_atual}, Pilha: {apd.pilha}\n")
        else:
            self.text_output.insert(tk.END, "\n❌ Poção incompleta ou instável.\n")
            self.text_output.insert(tk.END, f"Estado final: {apd.estado_atual}, Pilha: {apd.pilha}\n")

    def executar_frankenstein(self):
        self.text_output.delete('1.0', tk.END)
        frank = MooreFrankenstein()

        while True:
            parte = simpledialog.askstring("Frankenstein", "Adicione uma parte (cabeca, tronco, braco, perna):")
            if not parte:
                break

            frank.adicionar_parte(parte)
            self.text_output.insert(tk.END, f"{frank.saida_estado()}\n")

            if frank.estado == 'COMPLETO':
                try:
                    imagem = tk.PhotoImage(file="imagens/frankstain.png")  # ajuste o nome do arquivo corretamente!
                    self.imagem_frank = imagem  # manter referência para não perder a imagem
                   # self.text_output.insert(tk.END, "\n🧟 Frankenstein FINALIZADO:\n")
                    self.text_output.image_create(tk.END, image=self.imagem_frank)
                    self.text_output.insert(tk.END, "\n\n")
                except Exception as e:
                    self.text_output.insert(tk.END, f"⚠️ Erro ao carregar imagem: {e}\n")
                break


    def executar_turing(self):
        self.text_output.delete('1.0', tk.END)
        palavra = simpledialog.askstring("Máquina de Turing", "Insira a palavra para validar palíndromo:")
        if not palavra:
            self.text_output.insert(tk.END, "Nenhuma palavra inserida.\n")
            return

        mt = MaquinaTuring(palavra)  # Passa palavra no construtor
        resultado = mt.executar()     # Chama método executar sem parâmetro
        self.text_output.insert(tk.END, f"Palavra: {palavra}\n")
        if resultado == 'aceita':
            self.text_output.insert(tk.END, "✅ É um palíndromo!\n")
        else:
            self.text_output.insert(tk.END, "❌ Não é um palíndromo.\n")

    def iniciar_mealy(self):
        self.mealy = MealyPocao()
        self.iniciar_interacao_mealy_gui()  # Mostra estado inicial e ingredientes

        # Remove botões antigos
        for btn in self.botoes_ingredientes:
            btn.destroy()
        self.botoes_ingredientes.clear()

        # Cria botões novos com emojis
        ingredientes = [
            ('gelo', '🧊 Gelo'), ('fogo', '🔥 Fogo'), ('agua', '💧 Água'), ('po_magico', '✨ Pó Mágico'), ('ervas', '🌿 Ervas')
        ]

        # Criar um frame para organizar os botões em linha
        ingrediente_frame = tk.Frame(self.root, bg="#f5f3ff")
        ingrediente_frame.pack(pady=5)

        for i, (nome, emoji) in enumerate(ingredientes):
            btn = tk.Button(ingrediente_frame, text=emoji, width=18, command=lambda n=nome: self.adicionar_ingrediente_mealy(n))
            btn.grid(row=0, column=i, padx=5, pady=5)
            self.botoes_ingredientes.append(btn)


    def iniciar_interacao_mealy_gui(self):
        self.text_output.delete('1.0', tk.END)
        self.text_output.insert(tk.END, "🧪 Bem-vindo ao Misturador de Poções Mealy!\n")
        self.text_output.insert(tk.END, f"Estado inicial da poção: {self.mealy.estado}\n")
        self.text_output.insert(tk.END, "Ingredientes disponíveis: ")

        for ingr in self.mealy.ingredientes:
            self.text_output.insert(tk.END, f"{ingr}, ")
            print("\n")

    def adicionar_ingrediente_mealy(self, ingrediente):
        mensagem = self.mealy.processar(ingrediente)
        self.text_output.insert(tk.END, f"{mensagem}\nEstado atual: {self.mealy.estado}\n")



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
