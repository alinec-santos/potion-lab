from automatos.afd import AFD

def main():
    caminho = "automatos/entradas/IngredientesAfd.txt"
    afd = AFD(caminho)
    afd.executar()

if __name__ == "__main__":
    main()
