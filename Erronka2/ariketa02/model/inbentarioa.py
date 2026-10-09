from model.produktua import Produktua

class Inbentarioa:
    def __init__(self):
        self.__produktuak: list[Produktua] = []

    def gehitu_produktua(self, izena: str, kopurua: int, prezioa: float,) -> Produktua:
        produktua_berria: Produktua = Produktua(izena, kopurua, prezioa)
        self.__produktuak.append(produktua_berria)
        
        return produktua_berria

    def kalkulatu_balio_totala(self) -> float:
        return sum(
            produktua.kopurua * produktua.prezioa
            for produktua in self.__produktuak
        )

    def __iter__(self) -> iter[Produktua]:
        return iter(self.__produktuak)

    def __bool__(self) -> bool:
        return bool(self.__produktuak)
