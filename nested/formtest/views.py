from django.views.generic import TemplateView


class FormTestView(TemplateView):
    template_name = "form.html"
