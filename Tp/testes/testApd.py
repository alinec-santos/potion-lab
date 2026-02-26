from automatos.apd import APD

def main():
    caminho = "automatos\entradas\IngredientesApd.txt"
    apd = APD(caminho)
    apd.executar()

if __name__ == "__main__":
    main()