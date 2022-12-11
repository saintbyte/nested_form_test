from django.db import models
from django.utils.translation import gettext_lazy as _


class Cardealership(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("Name"))

    @property
    def as_string(self):
        return self.name

    def __str__(self) -> str:
        return self.as_string

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
    order = models.IntegerField(default=0, null=True)

    @property
    def as_string(self):
        return self.name

    def __str__(self) -> str:
        return self.as_string

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")
        ordering = [
            "-cardealership",
        ]


class Specification(models.Model):
    car = models.ForeignKey("formtest.Car", on_delete=models.CASCADE)
    order = models.IntegerField(default=0, null=True)
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    value = models.CharField(max_length=128, verbose_name=_("Value"))

    @property
    def as_string(self):
        return self.name

    def __str__(self) -> str:
        return self.as_string

    class Meta:
        verbose_name = _("Specification")
        verbose_name_plural = _("Specifications")
        ordering = [
            "-car",
        ]
