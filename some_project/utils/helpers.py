from collections import OrderedDict


def add_fields_to_data(obj: object, data: OrderedDict) -> OrderedDict:
    """dataに管理項目を付与する.主にAPIの戻り値として返すデータを作成するために利用.
    :param object obj: 管理項目を設定したオブジェクト
    :param object obj: リクエスト
    :return: viewの名前(100文字を超える場合は後ろの100文字を返す)
    """
    sd_list = list(data.items())
    sd_list.insert(len(sd_list) - 1, ("cre_user_id", obj.cre_user_id))
    sd_list.insert(len(sd_list) - 1, ("cre_pgm_id", obj.cre_pgm_id))
    sd_list.insert(len(sd_list) - 1, ("cre_dt", obj.cre_dt))
    sd_list.insert(len(sd_list) - 1, ("upd_user_id", obj.upd_user_id))
    sd_list.insert(len(sd_list) - 1, ("upd_pgm_id", obj.upd_pgm_id))
    sd_list.insert(len(sd_list) - 1, ("upd_dt", obj.upd_dt))
    added_data = OrderedDict(sd_list)
    return added_data


def add_fields_to_create_data(obj: object, data: OrderedDict) -> OrderedDict:
    """dataに id と管理項目を付与する.主にデータ追加APIの戻り値として返すデータを作成するために利用."""
    sd_list = list(data.items())
    sd_list.insert(0, ("id", obj.id))
    added_data = OrderedDict(sd_list)
    added_data = add_fields_to_data(obj, added_data)
    return added_data


def resolve_view_name(request):
    """リクエストオブジェクトからviewの名前を返す関数
    :param request: リクエスト
    :return: viewの名前(100文字を超える場合は後ろの100文字を返す)
    """
    VIEW_CLASS_ATTRIBUTE_NAME = "view_class_name"

    # ViewSetの場合は属性を参照する
    if hasattr(request, VIEW_CLASS_ATTRIBUTE_NAME):
        return getattr(request, VIEW_CLASS_ATTRIBUTE_NAME)

    func = request.resolver_match.func
    if hasattr(func, "__self__"):
        view_real = func.__self__.__class__
    else:
        view_real = func

    return "{}.{}".format(view_real.__module__, view_real.__name__)[-100:]
