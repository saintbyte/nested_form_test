from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from formtest.models import Car
from formtest.models import Cardealership
from formtest.models import Specification
from nested_formset import nestedformset_factory


class CardealershipForm(ModelForm):
    inline = nestedformset_factory(
        Cardealership,
        Car,
        extra=1,
        fk_name="cardealership",
        nested_formset=inlineformset_factory(
            Car, Specification, fk_name="car", extra=1, fields="__all__"
        ),
    )

    class Meta:
        model = Cardealership
        fields = "__all__"
