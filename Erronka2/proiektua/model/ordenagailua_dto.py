from datetime import datetime

class OrdenagailuaDto:
    def __init__(self, id: int, ip_elbidea: str, sistema_eragilea: str, erosketa_data: datetime, azken_errebisioa: datetime, oharrak: str):
        self.id: int = id
        self.ip_elbidea: str = ip_elbidea
        self.sistema_eragilea: str = sistema_eragilea
        self.erosketa_data: datetime = erosketa_data
        self.azken_errebisioa: datetime = azken_errebisioa
        self.oharrak: str = oharrak
        
    def __str__(self) -> str:
        return f"Ordenagailua {self.id} - IP: {self.ip_elbidea}, Sistema Eragilea: {self.sistema_eragilea}, Erosketa Data: {self.erosketa_data}, Azken Errebisioa: {self.azken_errebisioa}, Oharrak: {self.oharrak}"