from dataclasses import dataclass
from datetime import datetime
from collections import OrderedDict
from utils.helpers import (
    add_fields_to_data,
    add_fields_to_create_data,
    resolve_view_name,
)


@dataclass
class SomeClass:
    id: int = 1
    name: str = "Tarou Test"
    cre_user_id: str = "cre1234"
    cre_pgm_id: str = "crepgm"
    cre_dt: datetime = datetime(2021, 9, 22, 9, 55, 28)
    upd_user_id: str = "upd1234"
    upd_pgm_id: str = "updpgm"
    upd_dt: datetime = datetime(2021, 9, 23, 9, 55, 28)


def test_add_fields_to_data():
    """test_add_fields_to_data のテスト"""
    o = SomeClass()
    pod = OrderedDict(
        [
            ("key1", "value1"),
            ("key2", "value2"),
        ]
    )
    rod = add_fields_to_data(o, pod)

    # 属性が作られていることの確認
    assert "cre_user_id" in rod
    assert "cre_pgm_id" in rod
    assert "cre_dt" in rod
    assert "upd_user_id" in rod
    assert "upd_pgm_id" in rod
    assert "upd_dt" in rod

    # 属性に正しい値が設定されていることの確認
    assert rod["cre_user_id"] == o.cre_user_id
    assert rod["cre_pgm_id"] == o.cre_pgm_id
    assert rod["cre_dt"] == o.cre_dt
    assert rod["upd_user_id"] == o.upd_user_id
    assert rod["upd_pgm_id"] == o.upd_pgm_id
    assert rod["upd_dt"] == o.upd_dt

    # 属性の順番が保証されていることの確認
    rlist = list(rod.items())
    print(rlist)
    assert rlist[0][0] == "key1"
    assert rlist[1][0] == "key2"
    assert rlist[2][0] == "cre_user_id"
    assert rlist[3][0] == "cre_pgm_id"
    assert rlist[4][0] == "cre_dt"
    assert rlist[5][0] == "upd_user_id"
    assert rlist[6][0] == "upd_pgm_id"
    assert rlist[7][0] == "upd_dt"
