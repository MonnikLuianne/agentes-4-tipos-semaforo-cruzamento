# Agentes de IA: Controle de Semáforo em Cruzamento

## 1. Descrição do projeto

Este projeto implementa e compara quatro arquiteturas de agentes inteligentes aplicadas ao controle de um cruzamento simplificado com dois fluxos de tráfego:

- Norte–Sul (NS);
- Leste–Oeste (LO).

Os veículos chegam ao cruzamento de maneira estocástica ao longo do tempo. Um agente inteligente é responsável por controlar o semáforo, decidindo qual fluxo deve permanecer com o sinal verde.

O objetivo é comparar diferentes arquiteturas de agentes e verificar quais apresentam melhor desempenho no controle do trânsito, considerando o equilíbrio entre redução das filas, redução do tempo de espera, quantidade de veículos atendidos e quantidade de trocas do semáforo.

As arquiteturas implementadas são:

1. Agente Reflexivo Simples;
2. Agente Baseado em Modelo;
3. Agente Orientado a Objetivos;
4. Agente Baseado em Utilidade.

---

## 2. Objetivo

O objetivo principal é analisar o comportamento das quatro arquiteturas de agentes em um mesmo ambiente de simulação e identificar quais estratégias apresentam melhor desempenho no controle do cruzamento.

São avaliadas as seguintes métricas:

- tempo médio de espera dos veículos;
- maior fila formada;
- quantidade de veículos atendidos;
- número de trocas do semáforo.

---

## 3. Ambiente de simulação

O ambiente representa um cruzamento simplificado com duas vias:

```text
             Norte
               |
               |
Oeste -------- + -------- Leste
               |
               |
              Sul
