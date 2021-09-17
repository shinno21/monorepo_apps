from django.contrib import admin

from some_api.models import Order, OrderDetail


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail


@admin.register(Order)
class OrderHeaderAdmin(admin.ModelAdmin):
    fields = ("order_person", "order_day", "description", "is_express", "status")
    list_display = (
        "order_person",
        "order_day",
        "description",
        "is_express",
        "status",
        "cre_dt",
        "upd_dt",
    )
    inlines = [OrderDetailInline]
