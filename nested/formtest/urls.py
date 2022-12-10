from django.urls import path
from formtest.views import FormTestView

urlpatterns = [
    path("", FormTestView.as_view()),
]
