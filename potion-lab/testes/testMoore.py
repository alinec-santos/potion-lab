from automatos.moore import MooreFrankenstein

if __name__ == "__main__":
    maquina = MooreFrankenstein()

    while True:
        entrada = input("Digite a parte a adicionar (cabeca, tronco, braco, perna) ou 'sair': ").strip().lower()
        if entrada == 'sair':
            break
        maquina.adicionar_parte(entrada)