from collections import OrderedDict


def add_fields_to_data(obj: object, data: OrderedDict) -> OrderedDict:
    """dataに管理項目を付与する.主にAPIの戻り値として返すデータを作成するために利用.
    :param object obj: 管理項目を設定したオブジェクト
    :param object obj: リクエスト
    :return: viewの名前(100文字を超える場合は後ろの100文字を返す)
    """
    sd_list = list(data.items())
    sd_list.insert(len(sd_list), ("cre_user_id", obj.cre_user_id))
    sd_list.insert(len(sd_list), ("cre_dt", obj.cre_dt))
    sd_list.insert(len(sd_list), ("upd_user_id", obj.upd_user_id))
    sd_list.insert(len(sd_list), ("upd_dt", obj.upd_dt))
    added_data = OrderedDict(sd_list)
    return added_data


def add_fields_to_create_data(obj: object, data: OrderedDict) -> OrderedDict:
    """dataに id と管理項目を付与する.主にデータ追加APIの戻り値として返すデータを作成するために利用."""
    sd_list = list(data.items())
    sd_list.insert(0, ("id", obj.id))
    added_data = OrderedDict(sd_list)
    added_data = add_fields_to_data(obj, added_data)
    return added_data
