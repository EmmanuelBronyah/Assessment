from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_or_add_user, name="get-users-or-add-user"),
    path("<str:user_id>/", views.update_or_delete_user, name="update-or-delete-user"),
]
