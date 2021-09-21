class BaseException(Exception):
    pass


class TargetRecordDoesNotExist(BaseException):
    """対象のレコードが存在しない"""


class NoReferenceToUpdatedDateTime(BaseException):
    """更新日時への参照が見つからない"""


class NoMatchReaderClass(BaseException):
    """マッチする読み込みクラスがありません"""


class NotSupported(BaseException):
    """サポートされていません"""
