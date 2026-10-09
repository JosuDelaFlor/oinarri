from ui.cli import irakurri_zenbaki_positiboa

def kalkulatu_prezio_finala(prezioa: float, deskontua: float) -> float:
    return prezioa * (1 - deskontua / 100)


def irakurri_deskontua():
    while True:
        deskontua: float = irakurri_zenbaki_positiboa("Sartu deskontua porzentajeakin: ")
        if deskontua <= 100:
            return deskontua

        print("Porzentajeakin 0 eta 100 artean egon behar du")


def main():
    print("Deskontuen kalkulagailua")

    while True:
        prezioa: float = irakurri_zenbaki_positiboa('Sartu produktuaren prezioa edo irteteko "0": ')
        if prezioa == 0:
            break

        deskontua: float = irakurri_deskontua()
        prezio_finala: float = kalkulatu_prezio_finala(prezioa, deskontua)
        print("Deskontua aplikatu ondorengo azken prezioa: "f"{prezio_finala:.2f}")

    print("Agur")


if __name__ == "__main__":
    main()