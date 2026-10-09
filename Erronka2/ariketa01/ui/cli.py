def irakurri_zenbaki_positiboa(mesua: str) -> float:
    while True:
        try:
            zenbakia = float(input(mesua)) 
        except ValueError:
            print("Sartu balio numeriko bat")
            continue

        if zenbakia < 0:
            print("Positiboa izan behar da")
            continue

        return zenbakia