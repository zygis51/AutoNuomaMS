import csv
from datetime import datetime
from klientas import Klientas
from transporto_priemone import Automobilis, Mikroautobusas

def issaugoti_i_faila(klientai, failas):
    with open(failas, 'w', newline='') as f:
        writer = csv.writer(f)
        for klientas in klientai:
            for nuoma in klientas.nuomos:
                if isinstance(nuoma, Automobilis):
                    writer.writerow([
                        klientas.vardas, "Automobilis", nuoma._marke, nuoma._numeris,
                        nuoma._metai, nuoma._durys, nuoma.ar_isnuomota(), str(datetime.today().date())
                    ])
                elif isinstance(nuoma, Mikroautobusas):
                    writer.writerow([
                        klientas.vardas, "Mikroautobusas", nuoma._marke, nuoma._numeris,
                        nuoma._metai, nuoma._vietos, nuoma.ar_isnuomota(), str(datetime.today().date())
                    ])

def nuskaityti_is_failo(failas):
    with open(failas, 'r') as f:
        reader = csv.reader(f)
        for eilute in reader:
            print(f"Įrašas: Klientas: {eilute[0]}, Tipas: {eilute[1]}, Marke: {eilute[2]}, "
                  f"Numeris: {eilute[3]}, Būsena: {eilute[6]}, Data: {eilute[7]}")

def importuoti_klientus_is_csv(failas):
    klientai_dict = {}
    with open(failas, 'r') as f:
        reader = csv.reader(f)
        for eilute in reader:
            vardas, tipas, marke, numeris, metai, spec, is_nuomota_str, data = eilute
            is_nuomota = True if is_nuomota_str == "Taip" else False
            metai = int(metai)
            spec = int(spec)

            if tipas == "Automobilis":
                transportas = Automobilis(numeris, marke, metai, spec, is_nuomota)
            elif tipas == "Mikroautobusas":
                transportas = Mikroautobusas(numeris, marke, metai, spec, is_nuomota)

            if vardas not in klientai_dict:
                klientai_dict[vardas] = Klientas(vardas)

            klientai_dict[vardas].prideti_nuoma(transportas)
    return list(klientai_dict.values())
