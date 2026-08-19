import random


class Cruzamento:
    """
    Ambiente que representa um cruzamento simplificado
    com dois fluxos de tráfego:

    NS = Norte-Sul
    LO = Leste-Oeste
    """

    def __init__(
        self,
        semente,
        probabilidade_chegada=0.3
    ):
        self.semente = semente
        self.probabilidade_chegada = probabilidade_chegada

        self.random = random.Random(semente)

        self.resetar()

    def resetar(self):

        self.fila_ns = []
        self.fila_lo = []

        self.tempo = 0
        self.semaforo = "NS"

        self.veiculos_atendidos_ns = 0
        self.veiculos_atendidos_lo = 0

        self.tempo_total_espera_ns = 0
        self.tempo_total_espera_lo = 0

        self.maior_fila = 0
        self.numero_trocas = 0

    def gerar_veiculos(self):
        """
        Gera veículos de forma estocástica.
        """

        if self.random.random() < self.probabilidade_chegada:
            self.fila_ns.append(self.tempo)

        if self.random.random() < self.probabilidade_chegada:
            self.fila_lo.append(self.tempo)

    def calcular_espera_atual(self, fila):
        """
        Calcula quanto os veículos que ainda estão na fila
        já esperaram.
        """

        return sum(
            self.tempo - chegada
            for chegada in fila
        )

    def atualizar_espera(self):
        """
        Acumula o tempo de espera de todos os veículos
        que permanecem nas filas.
        """

        self.tempo_total_espera_ns += len(self.fila_ns)
        self.tempo_total_espera_lo += len(self.fila_lo)

    def atender_veiculos(self):
        """
        Atende no máximo um veículo por intervalo de tempo,
        respeitando o semáforo.
        """

        if self.semaforo == "NS":

            if self.fila_ns:
                self.fila_ns.pop(0)
                self.veiculos_atendidos_ns += 1

        elif self.semaforo == "LO":

            if self.fila_lo:
                self.fila_lo.pop(0)
                self.veiculos_atendidos_lo += 1

    def atualizar_maior_fila(self):
        """
        Registra o maior tamanho de fila observado.
        """

        maior_atual = max(
            len(self.fila_ns),
            len(self.fila_lo)
        )

        self.maior_fila = max(
            self.maior_fila,
            maior_atual
        )

    def alterar_semaforo(self, novo_estado):
        """
        Altera o semáforo e registra a troca.
        """

        if novo_estado != self.semaforo:

            self.semaforo = novo_estado
            self.numero_trocas += 1

    def observar(self):
        """
        Retorna o estado atual do ambiente para o agente.
        """

        espera_atual_ns = self.calcular_espera_atual(
            self.fila_ns
        )

        espera_atual_lo = self.calcular_espera_atual(
            self.fila_lo
        )

        return {
            "NS": len(self.fila_ns),
            "LO": len(self.fila_lo),

            "espera_NS": espera_atual_ns,
            "espera_LO": espera_atual_lo,

            "atendidos_NS": self.veiculos_atendidos_ns,
            "atendidos_LO": self.veiculos_atendidos_lo,

            "tempo": self.tempo,
            "semaforo": self.semaforo
        }

    def passo(self):
        """
        Avança a simulação em um intervalo de tempo.
        """

        self.tempo += 1

        self.gerar_veiculos()

        self.atualizar_espera()

        self.atender_veiculos()

        self.atualizar_maior_fila()

    def obter_metricas(self):
        """
        Calcula as métricas da execução.
        """

        veiculos_atendidos = (
            self.veiculos_atendidos_ns
            + self.veiculos_atendidos_lo
        )

        espera_total = (
            self.tempo_total_espera_ns
            + self.tempo_total_espera_lo
        )

        if veiculos_atendidos > 0:
            tempo_medio_espera = (
                espera_total / veiculos_atendidos
            )
        else:
            tempo_medio_espera = 0

        return {
            "tempo_medio_espera": tempo_medio_espera,
            "maior_fila": self.maior_fila,
            "veiculos_atendidos": veiculos_atendidos,
            "trocas_semaforo": self.numero_trocas
        }