import csv
import math


def ler_resultados(caminho):
    """
    Lê os resultados das simulações a partir do arquivo CSV.
    """

    resultados = []

    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            resultados.append({
                "agente": linha["agente"],
                "semente": int(linha["semente"]),
                "tempo_medio_espera": float(
                    linha["tempo_medio_espera"]
                ),
                "maior_fila": int(
                    linha["maior_fila"]
                ),
                "veiculos_atendidos": int(
                    linha["veiculos_atendidos"]
                ),
                "trocas_semaforo": int(
                    linha["trocas_semaforo"]
                )
            })

    return resultados


def calcular_media(valores):
    """
    Calcula a média aritmética.
    """

    return sum(valores) / len(valores)


def calcular_desvio_padrao(valores):
    """
    Calcula o desvio padrão populacional.
    """

    media = calcular_media(valores)

    variancia = sum(
        (valor - media) ** 2
        for valor in valores
    ) / len(valores)

    return math.sqrt(variancia)


def analisar_agente(resultados, nome_agente):
    """
    Calcula estatísticas de um determinado agente.
    """

    dados = [
        resultado
        for resultado in resultados
        if resultado["agente"] == nome_agente
    ]

    metricas = [
        "tempo_medio_espera",
        "maior_fila",
        "veiculos_atendidos",
        "trocas_semaforo"
    ]

    estatisticas = {}

    for metrica in metricas:

        valores = [
            resultado[metrica]
            for resultado in dados
        ]

        estatisticas[metrica] = {
            "media": calcular_media(valores),
            "minimo": min(valores),
            "maximo": max(valores),
            "desvio_padrao": calcular_desvio_padrao(
                valores
            )
        }

    return estatisticas


def mostrar_estatisticas(estatisticas):
    """
    Exibe as estatísticas no terminal.
    """

    print("\n")
    print("=" * 80)
    print("ANÁLISE ESTATÍSTICA")
    print("=" * 80)

    for agente, metricas in estatisticas.items():

        print(f"\n{agente}")
        print("-" * 80)

        for metrica, valores in metricas.items():

            print(
                f"{metrica}:"
            )

            print(
                f"  Média: "
                f"{valores['media']:.2f}"
            )

            print(
                f"  Mínimo: "
                f"{valores['minimo']:.2f}"
            )

            print(
                f"  Máximo: "
                f"{valores['maximo']:.2f}"
            )

            print(
                f"  Desvio padrão: "
                f"{valores['desvio_padrao']:.2f}"
            )


def main():

    caminho = "resultados/resultados.csv"

    resultados = ler_resultados(caminho)

    nomes_agentes = sorted(
        set(
            resultado["agente"]
            for resultado in resultados
        )
    )

    estatisticas = {}

    for nome in nomes_agentes:

        estatisticas[nome] = analisar_agente(
            resultados,
            nome
        )

    mostrar_estatisticas(estatisticas)


if __name__ == "__main__":
    main()