"""Small string utilities for exercises and testing."""
from typing import Optional
import re


def reverse_string(s: str) -> str:
    """Return the reverse of the input string.

    Raises TypeError if input is not a str.
    """
    if not isinstance(s, str):
        raise TypeError("s must be a str")
    return s[::-1]


def is_palindrome(s: str, ignore_case: bool = True, ignore_non_alnum: bool = True) -> bool:
    """Return True if s is a palindrome.

    ignore_case: compare case-insensitively
    ignore_non_alnum: ignore characters that are not letters/digits
    """
    if not isinstance(s, str):
        raise TypeError("s must be a str")
    t = s
    if ignore_non_alnum:
        t = re.sub(r"[^0-9A-Za-z]+", "", t)
    if ignore_case:
        t = t.lower()
    return t == t[::-1]


def count_vowels(s: str) -> int:
    """Count vowels (aeiou) in ASCII sense. Raises TypeError for non-str."""
    if not isinstance(s, str):
        raise TypeError("s must be a str")
    return sum(1 for ch in s.lower() if ch in "aeiou")


def camel_to_snake(name: str) -> str:
    """Convert CamelCase or camelCase to snake_case.

    Simple implementation using regex.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a str")
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.replace('-', '_').lower()


def truncate(s: str, max_len: int, ellipsis: bool = True) -> str:
    """Truncate string to max_len characters. If ellipsis is True and truncated,
    append '...' (counts towards max_len).
    """
    if not isinstance(s, str):
        raise TypeError("s must be a str")
    if not isinstance(max_len, int) or max_len < 0:
        raise ValueError("max_len must be non-negative int")
    if len(s) <= max_len:
        return s
    if max_len == 0:
        return "" if not ellipsis else "..."[:max_len]
    if ellipsis and max_len > 3:
        return s[: max_len - 3] + "..."
    return s[:max_len]
