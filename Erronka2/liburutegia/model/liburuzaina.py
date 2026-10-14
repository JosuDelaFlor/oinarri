from liburutegia.model.liburua import Liburua

class Liburuzaina:
    def __init__(self, izena: str):
        self.izena = izena
        self.__liburuak: list[Liburua] = []

    def liburua_gehitu(self, liburua: Liburua) -> None:
        if liburua not in self.__liburuak:
            self.__liburuak.append(liburua)

    def eskuragarri_dauden_liburuak_ikusi(self) -> None:
        print(f"\n=== {self.izena} liburuzainaren liburu eskuragarriak ===")
        liburu_eskuragarriak = [
            liburua for liburua in self.__liburuak if liburua.eskuragarri
        ]

        if not liburu_eskuragarriak:
            print("Ez dago liburu eskuragarririk")
            return

        for liburua in liburu_eskuragarriak:
            print(f"- {liburua}")