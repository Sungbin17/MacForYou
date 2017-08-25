from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^$",
        view=views.suggestions_create,
        name="create"
    )
]