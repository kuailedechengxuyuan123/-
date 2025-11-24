import unittest

from src import string_utils


class TestStringUtils(unittest.TestCase):

    def test_reverse_string_basic(self):
        self.assertEqual(string_utils.reverse_string('abc'), 'cba')
        self.assertEqual(string_utils.reverse_string(''), '')

    def test_reverse_string_type_error(self):
        with self.assertRaises(TypeError):
            string_utils.reverse_string(123)

    def test_is_palindrome_default(self):
        self.assertTrue(string_utils.is_palindrome('A man, a plan, a canal: Panama'))
        self.assertTrue(string_utils.is_palindrome('racecar'))
        self.assertFalse(string_utils.is_palindrome('hello'))

    def test_is_palindrome_options(self):
        self.assertFalse(string_utils.is_palindrome('Madam', ignore_case=False))
        self.assertTrue(string_utils.is_palindrome('Madam', ignore_case=True))
        self.assertTrue(string_utils.is_palindrome('No lemon, no melon', ignore_non_alnum=True))

    def test_count_vowels(self):
        self.assertEqual(string_utils.count_vowels('abcde'), 2)
        self.assertEqual(string_utils.count_vowels(''), 0)
        self.assertEqual(string_utils.count_vowels('AEIOU'), 5)
        with self.assertRaises(TypeError):
            string_utils.count_vowels(None)

    def test_camel_to_snake(self):
        self.assertEqual(string_utils.camel_to_snake('CamelCaseWord'), 'camel_case_word')
        self.assertEqual(string_utils.camel_to_snake('camelCase'), 'camel_case')
        self.assertEqual(string_utils.camel_to_snake('HTTPServerError'), 'http_server_error')
        with self.assertRaises(TypeError):
            string_utils.camel_to_snake(123)

    def test_truncate(self):
        self.assertEqual(string_utils.truncate('hello', 10), 'hello')
        self.assertEqual(string_utils.truncate('hello world', 5, ellipsis=False), 'hello')
        self.assertEqual(string_utils.truncate('hello world', 8, ellipsis=True), 'hello...')
        self.assertEqual(string_utils.truncate('abcd', 0, ellipsis=False), '')
        with self.assertRaises(ValueError):
            string_utils.truncate('x', -1)


if __name__ == '__main__':
    unittest.main()
