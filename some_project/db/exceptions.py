# coding: utf-8
class CommonException(Exception):
    pass


class TargetRecordDoesNotExist(CommonException):
    """対象のレコードが存在しない"""


class NoReferenceToUpdatedDateTime(CommonException):
    """更新日時への参照が見つからない"""


class NoMatchReaderClass(CommonException):
    """マッチする読み込みクラスがありません"""


class NotSupported(CommonException):
    """サポートされていません"""
