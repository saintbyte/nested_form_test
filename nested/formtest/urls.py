from django.urls import path
from formtest.views import CardealershipListView
from formtest.views import CreateCardealershipView
from formtest.views import EditCardealershipView

urlpatterns = [
    path("", CardealershipListView.as_view(), name="cardealership-list"),
    path("new/", CreateCardealershipView.as_view(), name="cardealership-create"),
    path("edit/<pk>", EditCardealershipView.as_view(), name="cardealership-edit"),
]
