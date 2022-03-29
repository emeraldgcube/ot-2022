import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")


    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")


    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(4)
        self.assertEqual(str(self.maksukortti), "saldo: 0.14")


    def test_rahan_ottaminen_toimii_kun_saldoa(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.08")


    def test_rahan_ottaminen_toimii_ei_saldoa(self):
        self.maksukortti.ota_rahaa(12)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_ottaminen_palauttaa_oikein_kun_saldoa(self):
        arvo=self.maksukortti.ota_rahaa(2)
        self.assertEqual((arvo), True)


    def test_rahan_ottaminen_palauttaa_oikein_ei_saldoa(self):
        arvo=self.maksukortti.ota_rahaa(12)
        self.assertEqual((arvo), False)