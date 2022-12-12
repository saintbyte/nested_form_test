from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from formtest.forms import CardealershipForm
from formtest.models import Cardealership


class CardealershipListView(ListView):
    model = Cardealership
    fields = "__all__"


class NestedFormMixin:
    """
    Миксин меняющий форму
    """

    def get_form_class(self):
        form = CardealershipForm
        return form


class CreateCardealershipView(NestedFormMixin, CreateView):
    model = Cardealership
    fields = "__all__"

    def get_template_names(self):
        return [
            "formtest/cardealersship_create.html",
        ]

    def get_success_url(self):
        return reverse("cardealership-list")


class EditCardealershipView(NestedFormMixin, UpdateView):
    model = Cardealership
    fields = "__all__"

    def get_template_names(self):
        return [
            "formtest/cardealersship_edit.html",
        ]

    def get_success_url(self):
        return reverse("cardealership-list")
