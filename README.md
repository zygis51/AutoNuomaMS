# AutoNuomaMS
# Kursinis darbas: Managment systems:Car Rental

## 1. Įvadas

### Kas yra ši programa?
Programa yra transporto valdymo sistema, leidžianti klientams nuomoti transporto priemones, tokias kaip automobiliai ir mikroautobusai. Sistema seka transporto priemonių informaciją, nuomos būseną ir klientų nuomas. Taip pat suteikia galimybę įrašyti ir perskaityti nuomos duomenis iš failo.

### Kaip paleisti programą?
Kodas yra įkeltas į GitHub, o naudojama Microsoft Visual Studio su Python:

1)Atsisiųsti kodą iš GitHub: Pirmiausia atidaryti Visual Studio, eiti į „File“ > „Clone Repository“ ir įvesti GitHub nuorodą į projektą. Pasirinkti vietą, kur išsaugoti projektą, ir spustelėti „Clone“.
2)Atidaryti projektą: Kai kodas bus atsisiųstas, atidaryti projektą Visual Studio. Pasirinkti „File“ > „Open“ > „Folder...“ ir surasti atsisiųstą kodą.
3)Paleisti programą: Spustelėti ant pagrindinio Python failo (pvz., programa.py), tada paspausti žalią trikampį „Start“ mygtuką arba paspausti F5. Programa pradės veikti ir matysis rezultatai.

### Kaip naudotis programa?
1. Naudotojas gali kurti transporto priemonių objektus (automobilius, mikroautobusus) naudojant `TransportoPriemoniuGamykla` klasę.
2. Klientai gali pridėti transporto priemones į savo nuomos sąrašą ir peržiūrėti nuomos informaciją.
3. Duomenys gali būti išsaugoti CSV faile naudojant `issaugoti_i_faila()` ir perskaityti naudojant `nuskaityti_is_failo()`.

## 2. Kodo Analizė

### Programos įgyvendinimo paaiškinimas

Programa įgyvendina objektinio programavimo principus, kad valdytų įvairių tipų transporto priemones ir jų nuomas.

### OOP principai ir jų taikymas:

1. **Polimorfizmas**:
   - Programa naudoja polimorfizmą, apibrėždama `TransportoPriemone` pagrindinę klasę ir perrašydama `gauti_info()` metodą `Automobilis` ir `Mikroautobusas` pogrupiuose. Tai leidžia skirtingiems transporto tipams grąžinti specifinę informaciją apie save, tačiau laikytis bendros sąsajos.
   - Kodo pavyzdys:
     ```python
     class Automobilis(TransportoPriemone):
         def gauti_info(self):
             return f"Automobilis: {self._marke} ({self._metai}), numeris: {self._numeris}, durys: {self._durys}"
     ```

2. **Abstrakcija**:
   - `TransportoPriemone` klasė abstrahuoja bendras savybes ir elgsenas transporto priemonėms, o pogrupiai pateikia konkrečius įgyvendinimus automobiliams ir mikroautobusams.
   - Pagrindinė klasė `TransportoPriemone` atskleidžia tik svarbius metodus, tokius kaip `ar_isnuomota()`, ir slepia detales apie transporto priemonės įgyvendinimą.
   - Kodo pavyzdys:
     ```python
     class TransportoPriemone(ABC):
         def __init__(self, numeris, marke, metai, is_nuomota=True):
             self._numeris = numeris
             self._marke = marke
             self._metai = metai
             self._is_nuomota = is_nuomota
     ```

3. **Paveldėjimas**:
   - Klasės `Automobilis` ir `Mikroautobusas` paveldi iš `TransportoPriemone` klasės, todėl gali pasinaudoti jos savybėmis ir metodais.
   - Tai leidžia suskirstyti transporto priemones pagal jų tipus ir naudoti bendrus metodus.
   - Kodo pavyzdys:
     ```python
     class Automobilis(TransportoPriemone):
         def __init__(self, numeris, marke, metai, durys, is_nuomota=True):
             super().__init__(numeris, marke, metai, is_nuomota)
             self._durys = durys
     ```

4. **Encapsuliacija**:
   - Programoje transporto priemonių savybės yra paslėptos ir gali būti pasiekiamos tik per metodus, tokius kaip `ar_isnuomota()`. Tai užtikrina, kad programos naudotojai gali keisti tik reikalingas savybes.
   - Kodo pavyzdys:
     ```python
     def ar_isnuomota(self):
         return "Taip" if self._is_nuomota else "Ne"
     ```

### Dizaino šablonas

Programa naudoja **Factory** dizaino šabloną, kad sukurtų skirtingų tipų transporto priemones (`Automobilis`, `Mikroautobusas`). Tai leidžia dinamiškai kurti įvairių tipų transporto priemones pagal poreikį ir centralizuotai valdyti jų kūrimą.

- Kodo pavyzdys:
  ```python
  class TransportoPriemoniuGamykla:
      @staticmethod
      def sukurti_transporto_priemone(tipas, **kwargs):
          if tipas == "automobilis":
              return Automobilis(**kwargs)
          elif tipas == "mikroautobusas":
              return Mikroautobusas(**kwargs)
          else:
              raise ValueError("Nežinomas transporto priemonės tipas.")
