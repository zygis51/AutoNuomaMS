from transporto_priemone import TransportoPriemoniuGamykla
from klientas import Klientas
from failo_apdorojimas import issaugoti_i_faila, nuskaityti_is_failo, importuoti_klientus_is_csv

if __name__ == "__main__":
    gamykla = TransportoPriemoniuGamykla()
    masina1 = gamykla.sukurti_transporto_priemone(
        "automobilis", numeris="ABC123", marke="Toyota", metai=2020, durys=4, is_nuomota=True)
    masina2 = gamykla.sukurti_transporto_priemone(
        "mikroautobusas", numeris="XYZ456", marke="Ford", metai=2018, vietos=8, is_nuomota=False)

    klientas = Klientas("Jonas")
    klientas.prideti_nuoma(masina1)
    klientas.prideti_nuoma(masina2)

    klientai = [klientas]
    issaugoti_i_faila(klientai, "nuomos_duomenys.csv")

    print("\n== Duomenys iš failo ==")
    nuskaityti_is_failo("nuomos_duomenys.csv")

    print("\n== Atkurtos nuomos ==")
    atkurti_klientai = importuoti_klientus_is_csv("nuomos_duomenys.csv")
    for k in atkurti_klientai:
        print(f"Klientas: {k.vardas}")
        k.parodyti_nuomas()
