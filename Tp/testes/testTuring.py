from automatos.turing import MaquinaTuring

palavra = input("Digite uma palavra para verificar se é um palíndromo (Sem X): ").strip().lower()
mt = MaquinaTuring(palavra)
mt.executar()
