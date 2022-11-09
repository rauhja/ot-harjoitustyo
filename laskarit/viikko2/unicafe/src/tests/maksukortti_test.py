import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortti_lataa_rahaa_oikein(self):
        self.maksukortti.lataa_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 25.00 euroa")

    def test_saldo_ei_muutu_jos_ei_ole_tarpeeksi_rahaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(2000))
    
    def test_saldo_muuttuu_jos_rahaa_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))
    