from liburutegia.model.liburua import Liburua
from liburutegia.model.erabiltzailea import Erabiltzailea
from liburutegia.model.liburuzaina import Liburuzaina


def main():
    liburua1 = Liburua("Cien años de soledad", "Gabriel García Márquez")
    liburua2 = Liburua("1984", "George Orwell")
    liburua3 = Liburua("Printze Txikia", "Antoine de Saint-Exupéry")

    liburuzaina = Liburuzaina("Niko")
    liburuzaina.liburua_gehitu(liburua1)
    liburuzaina.liburua_gehitu(liburua2)
    liburuzaina.liburua_gehitu(liburua3)

    erabiltzailea1 = Erabiltzailea("Irati")
    erabiltzailea2 = Erabiltzailea("Xabat")

    erabiltzailea1.maileguan_hartu(liburua1)
    erabiltzailea2.maileguan_hartu(liburua2)

    erabiltzailea1.informazioa_ikusi()
    erabiltzailea2.informazioa_ikusi()
    liburuzaina.eskuragarri_dauden_liburuak_ikusi()

    erabiltzailea1.liburua_itzuli(liburua1)

    erabiltzailea1.informazioa_ikusi()
    liburuzaina.eskuragarri_dauden_liburuak_ikusi()

if __name__ == "__main__":
    main()