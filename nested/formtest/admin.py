from django.contrib import admin
from formtest.models import Cardealership


class CardealershipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cardealership, CardealershipAdmin)
