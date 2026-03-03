# afd.py
from graphviz import Digraph
import tkinter as tk
from tkinter import simpledialog, messagebox 
class AFD:
    def __init__(self, caminho_arquivo):
        self.estados = []
        self.estado_inicial = ""
        self.estado_final = ""
        self.transicoes = {}  # Ex: {('I', 'a'): 'ing1'}
        self.estado_atual = ""
        self.estado_erro = "erro"
        self.carregar_arquivo(caminho_arquivo)

    def carregar_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip()]
        
        for i, linha in enumerate(linhas):
            if linha.startswith("Q:"):
                self.estados = linha[3:].split()
            elif linha.startswith("I:"):
                self.estado_inicial = linha[3:].strip()
                self.estado_atual = self.estado_inicial
            elif linha.startswith("F:"):
                self.estado_final = linha[3:].strip()
            elif linha == "---":
                break
            else:
                partes = linha.split("->")
                origem = partes[0].strip()
                destino, simbolos_str = partes[1].split("|")
                destino = destino.strip()
                simbolos = simbolos_str.strip().split()
                for simbolo in simbolos:
                    self.transicoes[(origem, simbolo)] = destino

    def resetar(self):
        self.estado_atual = self.estado_inicial

    def transitar(self, simbolo):
        chave = (self.estado_atual, simbolo)
        if chave in self.transicoes:
            proximo_estado = self.transicoes[chave]
            print(f"> {self.estado_atual} --[{simbolo}]--> {proximo_estado}")
            self.estado_atual = proximo_estado
        else:
            print(f"> Transição inválida com '{simbolo}'. Indo para o estado de erro.")
            self.estado_atual = self.estado_erro

    def executar(self):
        print("🧪 Início da produção de poção!")
        while True:
            simbolo = input("Insira o símbolo do próximo ingrediente: ").strip()
            self.transitar(simbolo)

            if self.estado_atual == self.estado_erro:
                break

            continuar = input("Deseja inserir mais um ingrediente? (s/n): ").strip().lower()
            if continuar != 's':
                break

        # Verificação final
        if self.estado_atual == self.estado_final:
            print("\n✅ Poção criada com sucesso!")
        else:
            print("\n❌ Erro na mistura.")

