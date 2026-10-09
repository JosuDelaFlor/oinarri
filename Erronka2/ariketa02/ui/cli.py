def irakurri_zenbaki_ez_negatiboa(mezua: str, zeroa_baimendu: bool=True) -> float:
    while True:
        try:
            zenbakia: float = float(input(mezua))
        except ValueError:
            print("Balio numerikoa izan behar du")
            continue

        if zenbakia < 0 or (not zeroa_baimendu and zenbakia == 0):
            print("Balioak >0 izan behar du")
            continue

        return zenbakia