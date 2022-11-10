import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10000)
    
    def test_kassassa_on_oikea_maara_rahaa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_riittava_maara_kateista(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_tasaraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_syo_maukkaasti_kateisella_riittava_maara_kateista(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_tasaraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_kortilla_riittava_maara_rahaa(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_riittava_maara_rahaa(self):
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_ei_riittava_maara_rahaa(self):
        kortti = Maksukortti(100)
        
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_ei_riittava_maara_rahaa(self):
        kortti = Maksukortti(100)
        
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 5000)
        
        self.assertEqual(self.kortti.saldo, 15000)
        self.assertEqual(self.kassa.kassassa_rahaa, 105000)
    
    def test_lataa_rahaa_kortille_nolla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 0)
        
        self.assertEqual(self.kortti.saldo, 10000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille_negatiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        
        self.assertEqual(self.kortti.saldo, 10000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)