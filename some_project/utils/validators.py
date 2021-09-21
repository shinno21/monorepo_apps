import re


def is_alnum_ascii(s):
    """ "文字列バリデーター（半角英数字）
    半角英数字以外はFalse
    """
    return True if re.fullmatch(r"[\d\w]+", s, re.ASCII) else False
