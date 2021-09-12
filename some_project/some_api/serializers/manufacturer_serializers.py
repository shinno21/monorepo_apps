# coding: utf-8
from rest_framework import serializers
from ..models import Manufacturer
from db.models import BaseModel
from utils.validators import is_alnum_ascii
from messages.error import ALNUM_ASCII_ERROR


class ManufacturerSerializer(serializers.ModelSerializer):
    """ManufacturerのSerializer"""

    class Meta:
        model = Manufacturer
        fields = [
            "cd",
            "name",
            "is_foreign",
        ] + [base_field.name for base_field in BaseModel._meta.get_fields()]

    def validate_cd(self, value):
        if not is_alnum_ascii(value):
            raise serializers.ValidationError(ALNUM_ASCII_ERROR.format(attr="コード"))
        return value