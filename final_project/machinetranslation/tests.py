import unittest
from unittest import TestCase

from translation import Translator

class test_french_to_english(TestCase):
    def test_translation(self):
        self.assertEqual(Translator().french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(Translator().french_to_english("War"),"Guerre")

    def test_null(self):
        self.assertEqual(Translator().french_to_english(""),"")


class test_english_to_french(TestCase):
    def test_translation(self):
        self.assertEqual(Translator().english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(Translator().english_to_french("Guerre"),"War")

    def test_null(self):
        self.assertEqual(Translator().english_to_french(""),"")

if __name__ == '__main__':
    unittest.main()