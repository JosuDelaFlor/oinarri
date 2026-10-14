class Liburua:
    def __init__(self, izenburua: str, egilea: str):
        self.izenburua = izenburua
        self.egilea = egilea
        self.eskuragarri = True

    def maileguan_ematea(self) -> bool:
        if not self.eskuragarri:
            return False

        self.eskuragarri = False
        return True

    def itzultzea(self) -> None:
        self.eskuragarri = True

    def __str__(self) -> str:
        return f"{self.izenburua} - {self.egilea}"