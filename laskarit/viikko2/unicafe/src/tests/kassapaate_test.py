import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa=Kassapaate()

    def test_rahamaara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_myytyjen_maara_oikea(self):
        myydyt=self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)

    def test_oston_jalkeen_kateisella_rahamaara_oikea(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_oston_jalkeen_kateisella_vaihtoraha_oikea(self):
        yo=self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(yo, 260)


    def test_oston_jalkeen_kateisella_rahamaara_oikea2(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_oston_jalkeen_kateisella_vaihtoraha_oikea2(self):
        yo=self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(yo, 100)


    def test_oston_jalkeen_kateisella_myydyt_edulliset_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_oston_jalkeen_kateisella_myydyt_maukkaat_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def kun_maksu_ei_riita_kateisella_edullisessa_niin_vaihtoraha_oikea(self):
        gong=self.kassa.syo_edullisesti_kateisella(239)
        self.assertEqual(gong, 239)

    def kun_maksu_ei_riita_kateisella_maukkaassa_niin_vaihtoraha_oikea(self):
        gang=self.kassa.syo_maukkaasti_kateisella(399)
        self.assertEqual(gang, 399)

    def test_oston_jalkeen_kateisella_myydyt_edulliset_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_oston_jalkeen_kateisella_myydyt_maukkaat_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def kun_maksu_ei_riita_kateisella_edullisessa_niin_vaihtoraha_oikea(self):
        gong=self.kassa.syo_edullisesti_kateisella(239)
        self.assertEqual(gong, 239)

    def kun_maksu_ei_riita_kateisella_maukkaassa_niin_vaihtoraha_oikea(self):
        gang=self.kassa.syo_maukkaasti_kateisella(399)
        self.assertEqual(gang, 399)


    def test_kun_maksu_ei_riita_kateisella_edulliseen_kassa_ei_kasva(self):
        self.kassa.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kun_maksu_ei_riita_kateisella_maukkaaseen_kassa_ei_kasva(self):
        self.kassa.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kun_maksu_ei_riita_kateisella_myydyt_edulliset_ei_kasva(self):
        self.kassa.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kun_maksu_ei_riita_kateisella_myydyt_maukkaat_ei_kasva(self):
        self.kassa.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_oston_jalkeen_kortilla_vastaus_oikea(self):
        kortti=Maksukortti(1000)
        yo=self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(yo, True)

    def test_oston_jalkeen_kortilla_vastaus_oikea2(self):
        kortti=Maksukortti(1000)
        yo=self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(yo, True)

    def test_epaonnistuneen_oston_jalkeen_kortilla_vastaus_oikea(self):
        kortti=Maksukortti(100)
        yo=self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(yo, False)

    def test_epaonnistuneen_oston_jalkeen_kortilla_vastaus_oikea2(self):
        kortti=Maksukortti(100)
        yo=self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(yo, False)

    def test_epaonnistuneen_oston_jalkeen_kortilla_myytyjen_maara_pysyy(self):
        kortti=Maksukortti(100)
        yo=self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_epaonnistuneen_oston_jalkeen_kortilla_myytyjen_maara_pysyy(self):
        kortti=Maksukortti(100)
        yo=self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_fail_oston_jalkeen_kortilta_ei_veloitettu_edullinen(self):
        kortti=Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_fail_oston_jalkeen_kortilta_ei_veloitettu_maukas(self):
        kortti=Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_oston_jalkeen_kortilla_kassa_ei_muutu(self):
        kortti=Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_oston_jalkeen_kortilla_kassa_ei_muutu2(self):
        kortti=Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_rahan_lataus_kassa_kasvaa(self):
        kortti=Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)


    def test_rahan_lataus_negatiivisella_kassa_pysyy(self):
        kortti=Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)


    def test_rahan_lataus_negatiivisella_saldo_pysyy(self):
        kortti=Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(kortti.saldo, 1000)


    def test_rahan_lataus_saldo_kasvaa(self):
        kortti=Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo, 1100)


