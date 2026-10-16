class SolairuaDto:
    def __init__(self, id: int, izena: str):
        self.id: int = id
        self.izena: str = izena
        
    def __str__(self) -> str:
        return f"Solairua {self.id} - {self.izena}"