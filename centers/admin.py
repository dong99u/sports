from django.contrib import admin
from .models import SportsCenter


@admin.register(SportsCenter)
class SportsCenterAdmin(admin.ModelAdmin):
    list_display = [
        "center_name",
        "phone_number",
        "get_road_address",
    ]
    search_fields = [
        "center_name",
        "phone_number",
        "road_address__address",
    ]
    list_filter = ["created_at", "updated_at"]

    def get_road_address(self, obj):
        return obj.road_address.address if obj.road_address else "-"

    get_road_address.short_description = "도로명 주소"
