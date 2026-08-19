from .modelo import Agente


class AgenteBaseadoUtilidade(Agente):
    """
    Agente baseado em utilidade.

    Avalia cada possível ação considerando:

    - tamanho das filas;
    - tempo de espera;
    - benefício de atender um veículo;
    - custo de trocar o semáforo.

    A decisão é tomada pela ação que apresenta
    maior utilidade.
    """

    def __init__(self):
        super().__init__("Baseado em Utilidade")

        self.peso_fila = 2.0
        self.peso_espera = 1.0
        self.peso_atendimento = 3.0
        self.custo_troca = 4.0

    def calcular_utilidade(
        self,
        fila_atendida,
        fila_espera,
        espera_atendida,
        espera_espera,
        atendimento,
        trocando
    ):
        """
        Calcula a utilidade de uma ação.

        A utilidade aumenta quando a ação:
        - atende uma via congestionada;
        - reduz uma fila;
        - reduz o tempo de espera.

        A utilidade diminui quando:
        - a outra via possui fila grande;
        - a outra via possui espera elevada;
        - é necessário trocar o semáforo.
        """

        utilidade = 0.0

        # Benefício relacionado à fila que será atendida.
        utilidade += (
            self.peso_fila * fila_atendida
        )

        # Benefício relacionado ao tempo de espera
        # da via que será atendida.
        utilidade += (
            self.peso_espera * espera_atendida
        )

        # Benefício de atender um veículo imediatamente.
        utilidade += (
            self.peso_atendimento * atendimento
        )

        # Penalização pela fila que ficará esperando.
        utilidade -= (
            self.peso_fila * fila_espera
        )

        # Penalização pela espera da outra via.
        utilidade -= (
            self.peso_espera * espera_espera
        )

        # Penalização por trocar o semáforo.
        if trocando:
            utilidade -= self.custo_troca

        return utilidade

    def decidir(self, percepcao):

        fila_ns = percepcao["NS"]
        fila_lo = percepcao["LO"]

        espera_ns = percepcao["espera_NS"]
        espera_lo = percepcao["espera_LO"]

        # Existe atendimento imediato se houver pelo
        # menos um veículo esperando.
        atendimento_ns = 1 if fila_ns > 0 else 0
        atendimento_lo = 1 if fila_lo > 0 else 0

        # -----------------------------------------------
        # AVALIAÇÃO DA AÇÃO NS
        # -----------------------------------------------

        utilidade_ns = self.calcular_utilidade(
            fila_atendida=fila_ns,
            fila_espera=fila_lo,
            espera_atendida=espera_ns,
            espera_espera=espera_lo,
            atendimento=atendimento_ns,
            trocando=self.estado != "NS"
        )

        # -----------------------------------------------
        # AVALIAÇÃO DA AÇÃO LO
        # -----------------------------------------------

        utilidade_lo = self.calcular_utilidade(
            fila_atendida=fila_lo,
            fila_espera=fila_ns,
            espera_atendida=espera_lo,
            espera_espera=espera_ns,
            atendimento=atendimento_lo,
            trocando=self.estado != "LO"
        )

        # -----------------------------------------------
        # DECISÃO
        # -----------------------------------------------

        if utilidade_ns > utilidade_lo:
            return "NS"

        if utilidade_lo > utilidade_ns:
            return "LO"

        # Em caso de empate, mantém o semáforo.
        return self.estado