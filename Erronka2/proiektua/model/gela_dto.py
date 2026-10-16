from proiektua.model.ordenagailua_dto import OrdenagailuaDto

class Gela_dto:
    def __init__(self, id: int, izena: str, ordenagailua: OrdenagailuaDto):
        self.id: int = id
        self.izena: str = izena
        self.ordenagailua: OrdenagailuaDto = ordenagailua
        
    def __str__(self) -> str:
        return f"Gela {self.id} - {self.izena} (Ordenagailua: {self.ordenagailua.id})"