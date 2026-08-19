from .modelo import Agente


class AgenteBaseadoModelo(Agente):
    """
    Agente baseado em modelo.

    Mantém informações sobre o comportamento anterior
    das filas e utiliza a tendência de crescimento para
    tomar decisões.
    """

    def __init__(self):
        super().__init__("Baseado em Modelo")

        self.fila_anterior_ns = 0
        self.fila_anterior_lo = 0

        # Evita trocas excessivamente frequentes.
        self.tempo_desde_troca = 0
        self.tempo_minimo_verde = 3

    def decidir(self, percepcao):

        fila_ns = percepcao["NS"]
        fila_lo = percepcao["LO"]

        crescimento_ns = (
            fila_ns - self.fila_anterior_ns
        )

        crescimento_lo = (
            fila_lo - self.fila_anterior_lo
        )

        self.fila_anterior_ns = fila_ns
        self.fila_anterior_lo = fila_lo

        self.tempo_desde_troca += 1

        # Impede troca muito rápida.
        if self.tempo_desde_troca < self.tempo_minimo_verde:
            return self.estado

        # Se NS está verde, avalia se LO está ficando
        # significativamente mais congestionada.
        if self.estado == "NS":

            if (
                fila_lo > fila_ns
                and crescimento_lo > crescimento_ns
            ):
                self.tempo_desde_troca = 0
                return "LO"

            return "NS"

        # Se LO está verde, avalia NS.
        if (
            fila_ns > fila_lo
            and crescimento_ns > crescimento_lo
        ):
            self.tempo_desde_troca = 0
            return "NS"

        return "LO"

    def resetar(self):

        super().resetar()

        self.fila_anterior_ns = 0
        self.fila_anterior_lo = 0

        self.tempo_desde_troca = 0