import unittest
from translator import __english_to_french__,__french_to_english__

class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(__english_to_french__(''),'') # test when '' is given as input the output is ''.
        self.assertEqual(__english_to_french__('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.
        


class TestFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(__french_to_english__(''),'') # test when '' is given as input the output is ''.
        self.assertEqual(__french_to_english__('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.


unittest.main()