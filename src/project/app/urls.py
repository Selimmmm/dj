from django.urls import path

from .views import index

urlpatterns = [
    # ex: /polls/
    path("", index, name="index"),
    # ex: /polls/5/
]
