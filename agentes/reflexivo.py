from .modelo import Agente


class AgenteReflexivo(Agente):
    """
    Agente reflexivo simples.

    Utiliza somente a situação atual das filas.

    Regra:
    - Se a via fechada possuir uma fila acima do limite,
      troca o semáforo.
    """

    def __init__(self, limite_fila=5):
        super().__init__("Reflexivo")
        self.limite_fila = limite_fila

    def decidir(self, percepcao):

        fila_ns = percepcao["NS"]
        fila_lo = percepcao["LO"]

        if self.estado == "NS":

            if fila_lo >= self.limite_fila:
                return "LO"

            return "NS"

        else:

            if fila_ns >= self.limite_fila:
                return "NS"

            return "LO"