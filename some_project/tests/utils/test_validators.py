# coding: utf-8
from utils.validators import is_alnum_ascii


def test_is_alnum_ascii():
    """is_alnum_asciiのテスト"""
    assert is_alnum_ascii("a1B2")
    assert is_alnum_ascii("a1B2-") is False
    assert is_alnum_ascii("a1B2あ") is False
