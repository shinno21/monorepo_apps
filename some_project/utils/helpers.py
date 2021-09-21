# coding: utf-8
from collections import OrderedDict


def add_fields_to_data(obj: object, data: OrderedDict) -> OrderedDict:
    """dataを管理項目を付与する"""
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
    """dataに id と管理項目を付与する(追加API用)"""
    sd_list = list(data.items())
    sd_list.insert(0, ("id", obj.id))
    added_data = OrderedDict(sd_list)
    added_data = add_fields_to_data(obj, added_data)
    return added_data
