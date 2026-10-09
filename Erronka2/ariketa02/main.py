from ui.cli import irakurri_zenbaki_ez_negatiboa

from model.inbentarioa import Inbentarioa
from model.produktua import Produktua

def irakurri_kopurua() -> None:
    while True:
        kopurua: int = irakurri_zenbaki_ez_negatiboa("Sartu kopurua: ", False)
        if kopurua.is_integer():
            return int(kopurua)

        print("Kopuruak zenbaki osoa izan behar du")

def erakutsi_inbentarioa(inbentarioa: Inbentarioa) -> None:
    print("\n=== Amaierako inbentarioa ===")
    if not inbentarioa:
        print("Inbentarioa hutsik dago")
    else:
        for produktua in inbentarioa:
            print(produktua.__str__())

    balio_totala: float = inbentarioa.kalkulatu_balio_totala()
    print(f"\nInbentarioaren balio guztira: {balio_totala:.2f}€")

def main():
    inbentarioa = Inbentarioa()
    print("=== Inbentarioaren kudeaketa ===")

    while True:
        izena: str = input("\nSartu produktuaren izena " "(edo 'irten' amaitzeko): ").strip()

        if izena.lower() == "irten":
            break
        
        if not izena:
            print("Balioa beteta egon behar da")
            continue
        
        kopurua: int = irakurri_kopurua()
        prezioa: float = irakurri_zenbaki_ez_negatiboa("Sartu unitateko prezioa: ", zeroa_baimendu=False)

        produktuaDto: Produktua = inbentarioa.gehitu_produktua(izena, kopurua, prezioa)
        print(
            f'Produktua gehituta: {produktuaDto.izena} - '
            f'{produktuaDto.kopurua} unitate - '
            f'{produktuaDto.prezioa:.2f}€ bakoitza'
        )

    erakutsi_inbentarioa(inbentarioa)

if __name__ == "__main__":
    main()