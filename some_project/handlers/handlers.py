from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status
from concurrency.exceptions import RecordModifiedError


def api_exception_handler(exc: Exception, context: dict) -> Response:
    """api が例外を投げた時のhandler
    * 排他制御エラー(HTTP 409) django-concurrency が RecordModifiedError を返す
    :param Exception exception: 管理項目を設定したオブジェクト
    :param dict context: APIインプットのserializer.data
    :return: dataにobjの管理項目を設定したOrderedDict
    """
    response = exception_handler(exc, context)
    if not response:
        if isinstance(exc, RecordModifiedError):
            err_data = {"MSG_HEADER": "Changes to the target object conflicted"}
            response = Response(err_data, status=status.HTTP_409_CONFLICT)
    return response
