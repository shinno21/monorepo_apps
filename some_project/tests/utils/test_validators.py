import pytest
from utils.validators import is_alnum_ascii


class TestIsAlnumAscii:
    """is_alnum_asciiのテスト"""

    @pytest.mark.parametrize("text", ["A1B2", "3c4d"])
    def test_valid(self, text):
        """検証が正しい場合"""
        assert is_alnum_ascii(text)

    @pytest.mark.parametrize("text", ["a1B2-", "a1B2あ", "", " "])
    def test_invalid(self, text):
        assert not is_alnum_ascii(text)
