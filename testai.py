import unittest
from transporto_priemone import Automobilis, Mikroautobusas
from klientas import Klientas
from failo_apdorojimas import issaugoti_i_faila, nuskaityti_is_failo

class TestTransportoPriemone(unittest.TestCase):

    def test_gauti_info_automobilis(self):
        automobilis = Automobilis(numeris="ABC123", marke="Toyota", metai=2020, durys=4, is_nuomota=True)
        info = automobilis.gauti_info()
        self.assertEqual(info, "Automobilis: Toyota (2020), numeris: ABC123, durys: 4")

    def test_gauti_info_mikroautobusas(self):
        mikroautobusas = Mikroautobusas(numeris="XYZ456", marke="Ford", metai=2018, vietos=8, is_nuomota=False)
        info = mikroautobusas.gauti_info()
        self.assertEqual(info, "Mikroautobusas: Ford (2018), numeris: XYZ456, vietų skaičius: 8")

    def test_ar_isnuomota(self):
        automobilis = Automobilis(numeris="ABC123", marke="Toyota", metai=2020, durys=4, is_nuomota=True)
        self.assertEqual(automobilis.ar_isnuomota(), "Taip")
        
        mikroautobusas = Mikroautobusas(numeris="XYZ456", marke="Ford", metai=2018, vietos=8, is_nuomota=False)
        self.assertEqual(mikroautobusas.ar_isnuomota(), "Ne")

    def test_issaugoti_i_faila(self):
        klientas = Klientas("Jonas")
        automobilis = Automobilis(numeris="ABC123", marke="Toyota", metai=2020, durys=4, is_nuomota=True)
        klientas.prideti_nuoma(automobilis)

        with open('test_nuomos_duomenys.csv', 'w', newline='') as f:
            issaugoti_i_faila([klientas], 'test_nuomos_duomenys.csv')

        with open('test_nuomos_duomenys.csv', 'r') as f:
            reader = csv.reader(f)
            eilute = next(reader)
            self.assertEqual(eilute[0], "Jonas")
            self.assertEqual(eilute[1], "Automobilis")
            self.assertEqual(eilute[2], "Toyota")
            self.assertEqual(eilute[3], "ABC123")
            self.assertEqual(eilute[6], "Taip")

    def test_nuskaityti_is_failo(self):
        with open('test_nuomos_duomenys.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Jonas", "Automobilis", "Toyota", "ABC123", "2020", "4", "Taip", str(datetime.today().date())])

        with open('test_nuomos_duomenys.csv', 'r') as f:
            output = StringIO()
            nuskaityti_is_failo('test_nuomos_duomenys.csv')
            output.seek(0)
            result = output.getvalue().strip()

        self.assertIn("Jonas", result)
        self.assertIn("Toyota", result)
        self.assertIn("ABC123", result)

if __name__ == "__main__":
    unittest.main()
