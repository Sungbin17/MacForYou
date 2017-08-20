from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^$",
        view=views.recommendation_create,
        name="create"
    )
]