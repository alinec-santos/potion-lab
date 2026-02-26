# Trabalho Prático  – Fundamentos da Teoria da Computação

## Sobre o projeto  

Este projeto foi desenvolvido na disciplina de Fundamentos da Teoria da Computação com o objetivo de implementar e simular diferentes modelos formais de computação.

O sistema consiste em uma aplicação interativa que utiliza autômatos para simular a validação e construção de sequências de entrada. O projeto contempla implementações obrigatórias de Autômato Finito Determinístico (AFD) e Autômato com Pilha (APD), além de extensões opcionais com Máquina de Mealy, Máquina de Moore e Máquina de Turing.

A aplicação pode ser executada tanto via terminal quanto por meio de interface gráfica desenvolvida em Tkinter.

---

## Objetivos  

- Implementar AFD e APD conforme especificação formal  
- Trabalhar com leitura de autômatos a partir de arquivos .txt  
- Simular transições de estados  
- Implementar estruturas de pilha para APD  
- Explorar modelos mais poderosos como Máquina de Turing  
- Desenvolver uma interface gráfica para interação com os autômatos  

---

## Autômatos Implementados  

### AFD  
- Leitura de definição formal a partir de arquivo .txt  
- Processamento determinístico de entrada  
- Estado de erro explícito  
- Execução interativa via terminal  
- Verificação de aceitação ao final da execução  

### APD  
- Leitura da definição formal via arquivo .txt  
- Manipulação de pilha (empilhar e desempilhar)  
- Transições com símbolo vazio  
- Verificação de aceitação por estado final e condição da pilha  

### Máquina de Mealy (Extra)  
- Saída associada à transição  
- Resposta dinâmica baseada em estado atual e entrada  
- Execução via terminal e interface  

### Máquina de Moore (Extra)  
- Saída associada ao estado  
- Simulação de montagem com mudança de estados  
- Atualização automática da saída conforme estado atual  

### Máquina de Turing (Extra)  
- Simulação de fita e cabeçote  
- Verificação de palíndromos  
- Marcação de símbolos durante execução  
- Demonstração de maior poder computacional  

---

## Interface Gráfica  

A interface foi desenvolvida utilizando Tkinter e permite:

- Executar todos os autômatos de forma visual  
- Inserir entradas interativamente  
- Visualizar transições e resultados  
- Reiniciar execuções  
- Exibir imagens e elementos gráficos  

A aplicação também mantém suporte completo para execução via terminal.

---

## Estrutura do Projeto  

- automatos/  
  Implementações do AFD, APD, Mealy, Moore e Turing  

- automatos/entradas/  
  Arquivos .txt com definições formais dos autômatos  

- interface/  
  Código da interface gráfica  

- testes/  
  Scripts para execução via terminal  

- imagens/  
  Recursos visuais utilizados na interface  

- README.md  

---

## Tecnologias Utilizadas  

- Python  
- Tkinter  
- Graphviz  

---

## Dependências  

Instalar a biblioteca necessária para visualização de estados:

pip install graphviz

---

## Como executar o projeto  

### Executar a interface gráfica  

python -m interface.app  

### Executar via terminal  

AFD:  
python -m testes.testAfd  

APD:  
python -m testes.testApd  

Mealy:  
python -m testes.testMealy  

Moore:  
python -m testes.testMoore  

Turing:  
python -m testes.testTuring  


