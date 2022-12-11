import nested_admin
from django.contrib import admin
from formtest.models import Car
from formtest.models import Cardealership
from formtest.models import Specification


class SpecificationInline(nested_admin.NestedStackedInline):
    model = Specification
    extra = 0
    sortable_field_name = "order"


class CarInline(nested_admin.NestedStackedInline):
    model = Car
    extra = 0
    sortable_field_name = "order"
    inlines = [SpecificationInline]


class CardealershipAdmin(nested_admin.NestedModelAdmin):
    inlines = [CarInline]


admin.site.register(Cardealership, CardealershipAdmin)
