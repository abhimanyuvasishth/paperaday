from django.urls import path

from . import views

urlpatterns = [
    path("", views.paper, name="paper"),
    path("archive", views.paper_archive, name="paper_archive"),
]
