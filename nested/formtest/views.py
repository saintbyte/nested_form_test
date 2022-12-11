from django.forms.models import inlineformset_factory
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from formtest.models import Car
from formtest.models import Cardealership
from formtest.models import Specification
from nested_formset import nestedformset_factory


class FormTestView(TemplateView):
    pass


class CardealershipListView(ListView):

    model = Cardealership
    fields = "__all__"


class CreateCardealershipView(CreateView):
    model = Cardealership
    fields = "__all__"

    def get_success_url(self):
        return reverse("cardealership-list")


class EditCardealershipView(UpdateView):

    model = Cardealership
    fields = "__all__"

    def get_template_names(self):
        return [
            "formtest/cardealersship_edit.html",
        ]

    def get_form_class(self):
        print("get_form_class")
        form = nestedformset_factory(
            Cardealership,
            Car,
            nested_formset=inlineformset_factory(Car, Specification, fields="__all__"),
        )
        return form

    def get_success_url(self):
        return reverse("cardealership-list")
