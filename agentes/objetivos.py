from .modelo import Agente


class AgenteOrientadoObjetivos(Agente):
    """
    Agente orientado a objetivos.

    Objetivo:
    manter as duas filas abaixo de um tamanho máximo.

    Diferentemente do agente reflexivo, este agente tenta
    avaliar o cumprimento de uma meta para as duas vias.
    """

    def __init__(self, limite_objetivo=4):
        super().__init__("Orientado a Objetivos")

        self.limite_objetivo = limite_objetivo

    def decidir(self, percepcao):

        fila_ns = percepcao["NS"]
        fila_lo = percepcao["LO"]

        # Verifica se cada fila está dentro do objetivo.
        ns_dentro_objetivo = fila_ns < self.limite_objetivo
        lo_dentro_objetivo = fila_lo < self.limite_objetivo

        # Se NS ultrapassou o objetivo, prioriza NS.
        if not ns_dentro_objetivo:

            # Se LO também estiver acima do objetivo,
            # atende primeiro a maior fila.
            if not lo_dentro_objetivo:

                if fila_ns >= fila_lo:
                    return "NS"

                return "LO"

            return "NS"

        # Se LO ultrapassou o objetivo, prioriza LO.
        if not lo_dentro_objetivo:
            return "LO"

        # As duas filas estão dentro do objetivo.
        # Calcula o quanto cada uma está próxima do limite.

        distancia_ns = (
            self.limite_objetivo - fila_ns
        )

        distancia_lo = (
            self.limite_objetivo - fila_lo
        )

        # Prioriza a fila que está mais próxima de
        # ultrapassar o objetivo.
        if distancia_ns < distancia_lo:
            return "NS"

        if distancia_lo < distancia_ns:
            return "LO"

        # Se estiverem igualmente distantes,
        # mantém o semáforo atual.
        return self.estado