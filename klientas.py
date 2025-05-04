class Klientas:
    def __init__(self, vardas):
        self.vardas = vardas
        self.nuomos = []

    def prideti_nuoma(self, transporto_priemone):
        self.nuomos.append(transporto_priemone)

    def parodyti_nuomas(self):
        for nuoma in self.nuomos:
            print(nuoma.gauti_info(), "| Išnuomota:", nuoma.ar_isnuomota())
