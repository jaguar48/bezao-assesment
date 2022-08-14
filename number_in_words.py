import inflect
from word2number import w2n
import unittest


im = inflect.engine()

while True:
    enter_text = input(" ENTER number in Digit or Words TO CONVERT  ")
    
    if enter_text.strip =="exit":
        print ("goodbye")
    if enter_text.strip().isdigit():
        def number_words():
            num = im.number_to_words(int(enter_text))
            return num + " naira"

        print(number_words())

    else: 
        def words_number():
            num = w2n.word_to_num(enter_text)
            return "#{:.2f}".format(num)
        print(words_number())
