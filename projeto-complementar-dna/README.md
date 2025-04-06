## Projeto Complementar DNA

**Descrição:** Retorna o nucleotídeo complementar (A, T, C, G).

## O que o projeto faz

Este projeto em Python solicita ao usuário que insira uma base nitrogenada (A, T, C ou G).  
Com base nessa entrada, o programa retorna a base complementar correspondente:  
- A ↔ T  
- C ↔ G  

Caso o usuário insira um caractere inválido, o programa exibe uma mensagem de erro.  
A lógica é baseada em estruturas condicionais `if/elif/else`.

## Exemplo de uso

Este código pode ser usado para validar sequências de DNA em pipelines de pré-processamento,  
onde é necessário gerar ou verificar fitas complementares antes de uma simulação molecular.

## Aplicação na bioinformática

Esse tipo de verificação é importante em:

- Algoritmos de **montagem de genoma**, onde as leituras são comparadas com suas fitas complementares;
- Ferramentas de **design de primers** para PCR, onde é necessário garantir complementaridade com a fita-alvo;
- Simulações estruturais, onde o pareamento de bases deve estar correto para gerar modelos de DNA tridimensionais;
- Programas que realizam **engenharia genética in silico**, garantindo integridade de sequências sintéticas.

Esse projeto é uma introdução prática à lógica condicional aplicada a dados genômicos.
