from django.db import models
from django.db.models import Model, AutoField, CharField, BigIntegerField
from datetime import datetime, timedelta
from django.db.models import CharField


def get_date(*args, **kwargs):
    return datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')


class Brigadier(Model):
    full_name = CharField(verbose_name="Ism Familya", max_length=50)
    tgid = BigIntegerField(verbose_name="Telegram ID", unique=True)
    username = CharField(verbose_name="Telegram Username", max_length=20, null=True)
    phone = CharField(max_length=13, null=True)

    class Meta:
        db_table = "bridgadier"
        verbose_name = "Brigadier"
        verbose_name_plural = "Brigadiers"

    def __str__(self):
        return self.full_name


class Object(models.Model):
    name = models.CharField(verbose_name="Obyekt nomi", max_length=56)
    location = models.CharField(verbose_name="Joylashuvi ", max_length=56)
    geolokatsiyasi = models.CharField(verbose_name="Geolokatsiyasi", max_length=512)

    class Meta:
        db_table = "object"
        verbose_name = "Obyekt"
        verbose_name_plural = "Obyektlar"

    def __str__(self):
        return self.name


class Staff(models.Model):
    full_name = models.CharField(verbose_name="Ism Familya", max_length=56)
    tgid = models.IntegerField(verbose_name="Telegram ID", unique=True, null=True, blank=True)
    username = models.CharField(verbose_name="Telegram Username",max_length=120, unique=True, null=True)

    class Meta:
        db_table = "stuff"
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"

    def __str__(self):
        return self.full_name

#
# class StaffReport(Model):
#     date = models.DateField("Sana", editable=True, value=get_date)
#     work_hour = models.DecimalField("Ish Smena", decimal_places=1, max_digits=3)
#     stuff_id = models.ForeignKey(verbose_name="Hodim", to=Staff, on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.date
#
# class CABack(Model):
#     brigadier_id = models.ForeignKey(verbose_name="Brigadir", to=Brigadier, on_delete=models.SET_NULL)
#     object = models.ForeignKey(verbose_name="Obyekt", to=Object, on_delete=models.SET_NULL, max_length=512)
#     location_name = models.CharField(verbose_name="Lokatsiya", max_length=512, on_delete=models.SET_NULL, null=True)
#     staff = models.ForeignKey(verbose_name="Hodim", to=Staff, max_length=56, on_delete=models.SET_NULL)
#     staff_postion = models.CharField(verbose_name="Hodim Lavozimi", max_length=56)
#     thour = models.ForeignKey(verbose_name="Jami ishlagan soati", decimal_places=1, null=True)
#     dwage = models.DecimalField(verbose_name="Kunlik Ish Haqi", decimal_places=2)
#     twage = models.DecimalField(verbose_name="Jami Kunlik Ish Haqi", decimal_places=2)
#
#     class Meta:
#         db_table = "caback"
#         verbose_name = "Keldi Ketdi"
#
#     def __str__(self):
#         return self.brigadier_id.__str__()
#
#
# class ToDoList(Model):
#     date = models.DateField(verbose_name="Sana", value=get_date(), unique=False)
#     brigadier = models.ForeignKey(verbose_name="Brigadir", Brigadier, on_delete=models.SET_NULL)
#     object = models.ForeignKey(Object, on_delete=models.SET_NULL)
#     stuff_count = models.IntegerField(null=False)
#     todos = models.TextField()
