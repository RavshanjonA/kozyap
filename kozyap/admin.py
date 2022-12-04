from django.contrib import admin

from kozyap.models import Staff, Object, Brigadier, StaffReport, ToDoList, Instrument, Transport, Driver


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "geolokatsiyasi"]


@admin.register(Brigadier)
class Brigadier(admin.ModelAdmin):
    list_display = ["full_name", "tgid", "username", "phone"]
    list_display_links = ["full_name", "tgid", "username", "phone"]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["full_name", "tgid", "username", "brigadier"]
    list_display_links = ["full_name", "tgid", "username", "brigadier"]


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ["owner", "status", "name", "number"]
    list_display_links = ["owner", "status", "name", "number"]


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ["name", "number", "company"]
    list_display_links = ["name", "number", "company"]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["fullname", "username", "phone", "tgid", "transport"]
    list_display_links = ["fullname", "username", "phone", "tgid", "transport"]


admin.site.register(StaffReport)
admin.site.register(ToDoList)
