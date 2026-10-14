from liburutegia.model.liburua import Liburua

class Erabiltzailea:
    def __init__(self, izena: str):
        self.izena = izena
        self.__mailegatutako_liburuak: list[Liburua] = []

    def maileguan_hartu(self, liburua: Liburua) -> bool:
        if not liburua.maileguan_ematea():
            print(f"Liburua ez dago eskuragarri: {liburua}")
            
            return False

        self.__mailegatutako_liburuak.append(liburua)
        print(f"{self.izena} erabiltzaileak liburua maileguan hartu du: {liburua}")
        
        return True

    def liburua_itzuli(self, liburua: Liburua) -> bool:
        if liburua not in self.__mailegatutako_liburuak:
            print(f"{self.izena} erabiltzaileak ez dauka liburu hau: {liburua}")
            
            return False

        self.__mailegatutako_liburuak.remove(liburua)
        liburua.itzultzea()
        print(f"{self.izena} erabiltzaileak liburua itzuli du: {liburua}")
        
        return True

    def informazioa_ikusi(self) -> None:
        print(f"\n=== {self.izena} erabiltzailearen informazioa ===")
        if not self.__mailegatutako_liburuak:
            print("Ez dauka mailegatutako libururik")
            
            return

        print("Mailegatutako liburuak:")
        for liburua in self.__mailegatutako_liburuak:
            print(f"- {liburua}")