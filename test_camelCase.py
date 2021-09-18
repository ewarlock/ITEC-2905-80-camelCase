import camelCase
import unittest

class TestCamelCase(unittest.TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual('thisIsAnAwesomeSentence', camelCase.camel_case('This is an AWESOME sentence'))

    def test_camelcase_newline_characters(self):
        self.assertEqual('thisIsAnAwesomeSentence', camelCase.camel_case('This \nis an AWESOME\n sentence'))

    def test_camelcase_punctuation(self):
        self.assertEqual('thi:;s[]IsAnAw\'esomeSen,tence!.?', camelCase.camel_case('Thi:;s [] is an AW\'ESOME sen,tence!.?'))

    def test_camelcase_multiple_spaces(self):
        self.assertEqual('thisIsAnAwesomeSentence', camelCase.camel_case(' This    is an   AWESOME        sentence     '))

    def test_camelcase_emoji(self):
        self.assertEqual('thisIsAn👻awesome👻Sentence', camelCase.camel_case('This is an 👻AWESOME👻 sentence'))

    def test_camelcase_not_emoji(self):
        self.assertEqual('', camelCase.camel_case(''))

    def test_is_sentence_valid_empty_string(self):
        sentence = ''
        self.assertFalse(camelCase.is_sentence_valid(sentence))
        
    def test_is_sentence_valid_only_spaces(self):
        sentence = '      '
        self.assertFalse(camelCase.is_sentence_valid(sentence))

    def test_is_sentence_valid_sentence(self):
        sentence = 'This IS the best SeNtence eVER!'
        self.assertTrue(camelCase.is_sentence_valid(sentence))


if __name__ == '__main__':
    unittest.main()

# python -m unittest test file name