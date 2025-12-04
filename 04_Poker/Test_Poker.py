import unittest

from Poker import Karte, flush, pair, strasse, full_house


class TestPoker(unittest.TestCase):
    def testFlush(self):
        karten = [Karte(12,0), Karte(5,0), Karte(2, 0), Karte(0, 0), Karte(7,0)]
        self.assertTrue(flush(karten),"Fehler")

        karten = [Karte(12,2), Karte(5,1), Karte(2, 0), Karte(0, 0), Karte(7,0)]
        self.assertFalse(flush(karten), "Fehler")

    def testPair(self):
        karten = [Karte(0, 0), Karte(0, 1), Karte(2, 0), Karte(3, 0), Karte(4, 0)]
        self.assertEqual(pair(karten), "one pair")

        karten = [Karte(0, 0), Karte(0, 1), Karte(2, 0), Karte(2, 1), Karte(4, 0)]
        self.assertEqual(pair(karten), "two pair")

    def test_strasse(self):
        karten = [Karte(0, 0), Karte(1, 1), Karte(2, 2), Karte(3, 3), Karte(4, 0)]
        self.assertTrue(strasse(karten))

    def test_full_house(self):
        # Test (3+2)
        karten = [Karte(0, 0), Karte(0, 1), Karte(0, 2), Karte(1, 0), Karte(1, 1)]
        self.assertTrue(full_house(karten))


if __name__ == "__main__":
    unittest.main()