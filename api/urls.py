from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="get-users-or-add-user"),
]
