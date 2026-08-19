class Agente:
    """
    Classe base para os agentes que controlam o semáforo.
    """

    def __init__(self, nome):
        self.nome = nome
        self.estado = "NS"

    def perceber(self, ambiente):
        """
        Obtém o estado atual do ambiente.
        """
        return ambiente.observar()

    def decidir(self, percepcao):
        """
        Cada arquitetura deve implementar sua própria decisão.
        """
        raise NotImplementedError

    def agir(self, ambiente):
        """
        Executa percepção, decisão e ação.
        """

        percepcao = self.perceber(ambiente)

        novo_estado = self.decidir(percepcao)

        ambiente.alterar_semaforo(novo_estado)

        self.estado = novo_estado

        return novo_estado

    def resetar(self):
        """
        Reinicia o estado do agente.
        """

        self.estado = "NS"