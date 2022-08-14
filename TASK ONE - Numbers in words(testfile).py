import inflect
from word2number import w2n
import unittest


im = inflect.engine()

def number_words(num):
    num = im.number_to_words(int(num))
    return num


print(number_words(124443))

def words_number(num):
    num = w2n.word_to_num(num)
    return num
print(words_number("seven hundred one"))

class TestNumbertowords(unittest.TestCase):

    def test_number_words(self):

        res = number_words(2)
        self.assertEqual(res, "two")
        
class TestWordtonumber(unittest.TestCase):

    def test_words_number(self):
    
        res = words_number("two")
        self.assertEqual(res, 2)

if __name__ == '__main__':
    unittest.main()
