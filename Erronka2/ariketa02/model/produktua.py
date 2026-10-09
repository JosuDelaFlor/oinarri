class Produktua:
    def __init__(self, izena: str, kopurua: int, prezioa: float):
        self.izena = izena
        self.kopurua = kopurua
        self.prezioa = prezioa

    def __str__(self) -> str:
        return f"{self.izena} - {self.kopurua} unitate - {self.prezioa:.2f} €"