from django.contrib import admin
from myapp.models import Event, Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']  # 页面显示那些字段
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']  # 过滤器


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
