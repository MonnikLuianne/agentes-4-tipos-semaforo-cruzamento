from ambiente.cruzamento import Cruzamento


def executar_simulacao(agente, semente, duracao=100):
    """
    Executa uma simulação para um agente e uma semente.
    """

    ambiente = Cruzamento(semente)

    agente.resetar()

    for _ in range(duracao):
        agente.agir(ambiente)
        ambiente.passo()

    metricas = ambiente.obter_metricas()

    metricas["agente"] = agente.nome
    metricas["semente"] = semente

    return metricas


def executar_experimentos(agentes, sementes, duracao=100):
    """
    Executa todos os agentes utilizando exatamente as
    mesmas sementes.

    Retorna uma lista contendo os resultados de todas
    as execuções.
    """

    resultados = []

    for semente in sementes:

        for agente in agentes:

            resultado = executar_simulacao(
                agente=agente,
                semente=semente,
                duracao=duracao
            )

            resultados.append(resultado)

    return resultados