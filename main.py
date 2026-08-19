import csv
import os

from agentes import (
    AgenteReflexivo,
    AgenteBaseadoModelo,
    AgenteOrientadoObjetivos,
    AgenteBaseadoUtilidade
)

from simulacao import executar_experimentos


def salvar_resultados(resultados):
    """
    Salva os resultados das simulações em um arquivo CSV.
    """

    os.makedirs("resultados", exist_ok=True)

    caminho = "resultados/resultados.csv"

    campos = [
        "agente",
        "semente",
        "tempo_medio_espera",
        "maior_fila",
        "veiculos_atendidos",
        "trocas_semaforo"
    ]

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        escritor.writeheader()

        escritor.writerows(resultados)

    print(f"\nResultados salvos em: {caminho}")


def mostrar_resumo(resultados):
    """
    Mostra a média das métricas de cada agente.
    """

    agentes = {}

    for resultado in resultados:

        nome = resultado["agente"]

        if nome not in agentes:
            agentes[nome] = []

        agentes[nome].append(resultado)

    print("\n")
    print("=" * 70)
    print("RESUMO DOS EXPERIMENTOS")
    print("=" * 70)

    for nome, resultados_agente in agentes.items():

        quantidade = len(resultados_agente)

        media_espera = sum(
            r["tempo_medio_espera"]
            for r in resultados_agente
        ) / quantidade

        media_fila = sum(
            r["maior_fila"]
            for r in resultados_agente
        ) / quantidade

        media_atendidos = sum(
            r["veiculos_atendidos"]
            for r in resultados_agente
        ) / quantidade

        media_trocas = sum(
            r["trocas_semaforo"]
            for r in resultados_agente
        ) / quantidade

        print(f"\n{nome}")
        print("-" * 50)

        print(
            f"Execuções: {quantidade}"
        )

        print(
            f"Tempo médio de espera: "
            f"{media_espera:.2f}"
        )

        print(
            f"Maior fila média: "
            f"{media_fila:.2f}"
        )

        print(
            f"Veículos atendidos (média): "
            f"{media_atendidos:.2f}"
        )

        print(
            f"Trocas do semáforo (média): "
            f"{media_trocas:.2f}"
        )


def main():

    # =====================================================
    # AGENTES
    # =====================================================

    agentes = [
        AgenteReflexivo(),
        AgenteBaseadoModelo(),
        AgenteOrientadoObjetivos(),
        AgenteBaseadoUtilidade()
    ]

    # =====================================================
    # PROTOCOLO EXPERIMENTAL
    # =====================================================

    quantidade_execucoes = 30

    sementes = range(
        42,
        42 + quantidade_execucoes
    )

    duracao = 100

    print("=" * 70)
    print("EXPERIMENTO COM OS QUATRO AGENTES")
    print("=" * 70)

    print(
        f"\nAgentes: {len(agentes)}"
    )

    print(
        f"Execuções por agente: "
        f"{quantidade_execucoes}"
    )

    print(
        f"Total de simulações: "
        f"{len(agentes) * quantidade_execucoes}"
    )

    print(
        f"Passos por simulação: "
        f"{duracao}"
    )

    print(
        f"Sementes: "
        f"{list(sementes)}"
    )

    # =====================================================
    # EXECUÇÃO
    # =====================================================

    resultados = executar_experimentos(
        agentes=agentes,
        sementes=sementes,
        duracao=duracao
    )

    # =====================================================
    # RESULTADOS
    # =====================================================

    salvar_resultados(resultados)

    mostrar_resumo(resultados)


if __name__ == "__main__":
    main()