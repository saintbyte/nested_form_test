from django.db import models
from django.utils.translation import gettext_lazy as _


class Cardealership(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Car dealership")
        verbose_name_plural = _("Car dealerships")
        ordering = [
            "-pk",
        ]


class Car(models.Model):
    cardealership = models.ForeignKey(
        "formtest.Cardealership", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")
        ordering = [
            "-cardealership",
        ]


class Specification(models.Model):
    car = models.ForeignKey("formtest.Car", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    value = models.CharField(max_length=128, verbose_name=_("Value"))

    class Meta:
        verbose_name = _("Specification")
        verbose_name_plural = _("Specifications")
        ordering = [
            "-car",
        ]
