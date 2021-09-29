import pytest
from dataclasses import dataclass
from datetime import datetime
from collections import OrderedDict
from utils.helpers import (
    add_fields_to_data,
    add_fields_to_create_data,
)


@dataclass
class SomeClass:
    id: int = 1
    name: str = "Tarou Test"
    cre_user_id: str = "cre1234"
    cre_dt: datetime = datetime(2021, 9, 22, 9, 55, 28)
    upd_user_id: str = "upd1234"
    upd_dt: datetime = datetime(2021, 9, 23, 9, 55, 28)


class TestAddFieldsToData:
    """test_add_fields_to_data のテスト"""

    ATTRS = [
        "cre_user_id",
        "cre_dt",
        "upd_user_id",
        "upd_dt",
    ]

    @pytest.fixture
    def param_objects(self):
        o = SomeClass()
        pod = OrderedDict(
            [
                ("key1", "value1"),
                ("key2", "value2"),
            ]
        )
        return (o, pod)

    @pytest.mark.parametrize("attrs", ATTRS)
    def test_valid_create_attrs(self, param_objects, attrs):
        """属性が作られていることの確認"""

        o, pod = param_objects
        rod = add_fields_to_data(o, pod)

        assert attrs in rod

    @pytest.mark.parametrize("attrs", ATTRS)
    def test_valid_create_value(self, param_objects, attrs):
        """属性に正しい値が設定されていることの確認"""

        o, pod = param_objects
        rod = add_fields_to_data(o, pod)

        assert rod[attrs] == getattr(o, attrs)

    def test_valid_sort_order(self, param_objects):
        """属性の順番が保証されていることの確認"""
        o, pod = param_objects
        rod = add_fields_to_data(o, pod)
        rlist = list(rod.items())

        assert rlist[0][0] == "key1"
        assert rlist[5][0] == "upd_dt"


class TestAddFieldsToCreateData:
    """add_fields_to_create_data のテスト"""

    ID_ATTRS = [
        "id",
        "cre_user_id",
        "cre_dt",
        "upd_user_id",
        "upd_dt",
    ]

    @pytest.fixture
    def param_objects(self):
        o = SomeClass()
        pod = OrderedDict(
            [
                ("key1", "value1"),
                ("key2", "value2"),
            ]
        )
        return (o, pod)

    @pytest.mark.parametrize("attrs", ID_ATTRS)
    def test_valid_create_attrs(self, param_objects, attrs):
        """属性が作られていることの確認"""

        o, pod = param_objects
        rod = add_fields_to_create_data(o, pod)

        assert attrs in rod

    @pytest.mark.parametrize("attrs", ID_ATTRS)
    def test_valid_create_value(self, param_objects, attrs):
        """属性に正しい値が設定されていることの確認"""

        o, pod = param_objects
        rod = add_fields_to_create_data(o, pod)

        assert rod[attrs] == getattr(o, attrs)

    def test_valid_sort_order(self, param_objects):
        """属性の順番が保証されていることの確認"""
        o, pod = param_objects
        rod = add_fields_to_create_data(o, pod)
        rlist = list(rod.items())
        assert rlist[0][0] == "id"
        assert rlist[1][0] == "key1"
        assert rlist[6][0] == "upd_dt"
