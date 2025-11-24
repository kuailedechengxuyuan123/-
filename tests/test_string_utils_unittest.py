import unittest

from src import string_utils


class TestStringUtils(unittest.TestCase):

    # reverse_string 边界值与等价类：
    # - 输入为空字符串（边界值）
    # - 输入为普通字符串（等价类）
    def test_reverse_string_basic(self):
        self.assertEqual(string_utils.reverse_string('abc'), 'cba')
        self.assertEqual(string_utils.reverse_string(''), '')

    # reverse_string 异常等价类：
    # - 输入非字符串类型（如 int），应抛出 TypeError
    def test_reverse_string_type_error(self):
        with self.assertRaises(TypeError):
            string_utils.reverse_string(123)

    # is_palindrome 边界值与等价类：
    # - 忽略大小写和非字母数字，典型回文（等价类）
    # - 非回文字符串（等价类）
    def test_is_palindrome_default(self):
        self.assertTrue(string_utils.is_palindrome('A man, a plan, a canal: Panama'))
        self.assertTrue(string_utils.is_palindrome('racecar'))
        self.assertFalse(string_utils.is_palindrome('hello'))

    # is_palindrome 参数变体：
    # - ignore_case=False（区分大小写，边界值）
    # - ignore_case=True（不区分大小写，等价类）
    # - ignore_non_alnum=True（忽略非字母数字，等价类）
    def test_is_palindrome_options(self):
        self.assertFalse(string_utils.is_palindrome('Madam', ignore_case=False))
        self.assertTrue(string_utils.is_palindrome('Madam', ignore_case=True))
        self.assertTrue(string_utils.is_palindrome('No lemon, no melon', ignore_non_alnum=True))

    # count_vowels 边界值与等价类：
    # - 输入为空字符串（边界值）
    # - 全为元音（边界值）
    # - 混合元音和非元音（等价类）
    # - 输入为 None（异常等价类，应抛 TypeError）
    def test_count_vowels(self):
        self.assertEqual(string_utils.count_vowels('abcde'), 2)
        self.assertEqual(string_utils.count_vowels(''), 0)
        self.assertEqual(string_utils.count_vowels('AEIOU'), 5)
        with self.assertRaises(TypeError):
            string_utils.count_vowels(None)

    # camel_to_snake 边界值与等价类：
    # - 普通 CamelCase（等价类）
    # - 首字母小写 camelCase（边界值）
    # - 连续大写（如 HTTPServerError，边界值）
    # - 输入非字符串（异常等价类，应抛 TypeError）
    def test_camel_to_snake(self):
        self.assertEqual(string_utils.camel_to_snake('CamelCaseWord'), 'camel_case_word')
        self.assertEqual(string_utils.camel_to_snake('camelCase'), 'camel_case')
        self.assertEqual(string_utils.camel_to_snake('HTTPServerError'), 'http_server_error')
        with self.assertRaises(TypeError):
            string_utils.camel_to_snake(123)

    # truncate 边界值与等价类：
    # - max_len 大于字符串长度（边界值）
    # - max_len 小于字符串长度，ellipsis=False（等价类）
    # - max_len 小于字符串长度，ellipsis=True（等价类）
    # - max_len=0（边界值）
    # - max_len 为负（异常等价类，应抛 ValueError）
    def test_truncate(self):
        self.assertEqual(string_utils.truncate('hello', 10), 'hello')
        self.assertEqual(string_utils.truncate('hello world', 5, ellipsis=False), 'hello')
        self.assertEqual(string_utils.truncate('hello world', 8, ellipsis=True), 'hello...')
        self.assertEqual(string_utils.truncate('abcd', 0, ellipsis=False), '')
        with self.assertRaises(ValueError):
            string_utils.truncate('x', -1)


if __name__ == '__main__':
    unittest.main()
