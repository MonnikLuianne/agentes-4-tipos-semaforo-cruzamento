import csv
import os

import matplotlib.pyplot as plt


def carregar_resultados():
    """
    Carrega os resultados das 120 simulações.
    """

    resultados = []

    with open(
        "resultados/resultados.csv",
        "r",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            resultados.append({
                "agente": linha["agente"],
                "tempo_medio_espera": float(
                    linha["tempo_medio_espera"]
                ),
                "maior_fila": float(
                    linha["maior_fila"]
                ),
                "veiculos_atendidos": float(
                    linha["veiculos_atendidos"]
                ),
                "trocas_semaforo": float(
                    linha["trocas_semaforo"]
                )
            })

    return resultados


def calcular_medias(resultados):
    """
    Calcula as médias das métricas para cada agente.
    """

    agentes = {}

    for resultado in resultados:

        nome = resultado["agente"]

        if nome not in agentes:
            agentes[nome] = []

        agentes[nome].append(resultado)

    medias = {}

    for nome, dados in agentes.items():

        quantidade = len(dados)

        medias[nome] = {
            "tempo_medio_espera": sum(
                d["tempo_medio_espera"]
                for d in dados
            ) / quantidade,

            "maior_fila": sum(
                d["maior_fila"]
                for d in dados
            ) / quantidade,

            "veiculos_atendidos": sum(
                d["veiculos_atendidos"]
                for d in dados
            ) / quantidade,

            "trocas_semaforo": sum(
                d["trocas_semaforo"]
                for d in dados
            ) / quantidade
        }

    return medias


def criar_grafico(
    medias,
    metrica,
    titulo,
    ylabel,
    nome_arquivo
):
    """
    Cria um gráfico de barras para uma métrica.
    """

    nomes = list(medias.keys())

    valores = [
        medias[nome][metrica]
        for nome in nomes
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(nomes, valores)

    plt.title(titulo)

    plt.ylabel(ylabel)

    plt.xticks(
        rotation=15,
        ha="right"
    )

    plt.tight_layout()

    caminho = os.path.join(
        "graficos",
        nome_arquivo
    )

    plt.savefig(
        caminho,
        dpi=300
    )

    plt.close()

    print(f"Gráfico salvo: {caminho}")


def main():

    os.makedirs(
        "graficos",
        exist_ok=True
    )

    resultados = carregar_resultados()

    medias = calcular_medias(resultados)

    criar_grafico(
        medias,
        "tempo_medio_espera",
        "Tempo Médio de Espera por Agente",
        "Tempo médio de espera",
        "tempo_medio_espera.png"
    )

    criar_grafico(
        medias,
        "maior_fila",
        "Maior Fila Média por Agente",
        "Tamanho médio da maior fila",
        "maior_fila.png"
    )

    criar_grafico(
        medias,
        "veiculos_atendidos",
        "Média de Veículos Atendidos por Agente",
        "Veículos atendidos",
        "veiculos_atendidos.png"
    )

    criar_grafico(
        medias,
        "trocas_semaforo",
        "Número Médio de Trocas do Semáforo",
        "Trocas do semáforo",
        "trocas_semaforo.png"
    )


if __name__ == "__main__":
    main()