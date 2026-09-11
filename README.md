# Controle Remoto POO em Python

Projeto desenvolvido em Python para praticar conceitos de Programação Orientada a Objetos (POO), simulando o funcionamento de um controle remoto de televisão através do terminal.

## Sobre o projeto

O programa simula uma televisão controlada por um controle remoto, permitindo ligar e desligar a TV, alterar canais e ajustar o volume.

O projeto foi desenvolvido como parte dos estudos de Programação Orientada a Objetos no curso de Python do Curso em Vídeo, com foco na aplicação prática de classes, atributos, métodos e regras de comportamento de objetos.

## Funcionalidades

* Ligar e desligar a televisão
* Aumentar e diminuir o volume
* Alterar o canal para cima ou para baixo
* Navegação circular entre os canais
* Controle dos limites mínimo e máximo de volume
* Bloqueio das funções de canal e volume quando a TV está desligada
* Exibição do estado atual da televisão no terminal
* Interface visual utilizando Rich

## Conceitos praticados

Durante o desenvolvimento foram trabalhados conceitos como:

* Classes e objetos
* Construtor `__init__`
* Atributos de instância
* Métodos
* Encapsulamento de comportamentos
* Condicionais
* Estruturas `match/case`
* Validação de limites
* Manipulação do estado de um objeto
* Uso de bibliotecas externas em Python

## Tecnologias

* Python
* Rich
* uv
* Git
* GitHub

## Como executar

Clone o repositório:

```bash
git clone https://github.com/jp-lira01/controle-remoto-poo-python.git
```

Entre na pasta do projeto:

```bash
cd controle-remoto-poo-python
```

Instale as dependências:

```bash
uv sync
```

Execute o programa:

```bash
python Controle_remoto.py
```

## Controles

| Tecla | Função             |
| ----- | ------------------ |
| `@`   | Liga/desliga a TV  |
| `<`   | Canal anterior     |
| `>`   | Próximo canal      |
| `-`   | Diminui o volume   |
| `+`   | Aumenta o volume   |
| `0`   | Encerra o programa |

## Estrutura

```text
controle-remoto-poo-python/
├── .gitignore
├── Controle_remoto.py
├── README.md
├── pyproject.toml
└── uv.lock
```

## Objetivo

O objetivo principal deste projeto é consolidar os fundamentos de Programação Orientada a Objetos em Python por meio de uma aplicação simples, mas que envolve diferentes regras de comportamento e interação entre atributos e métodos.

## Autor

**João Pedro de Lira Franco**

[LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-pedro-de-lira-franco-aa30a6421/)

[GitHub](https://github.com/jp-lira01)
