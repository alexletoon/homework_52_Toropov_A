from django.urls import path

from list_app import views


urlpatterns = [
    path("", views.index_view)
]