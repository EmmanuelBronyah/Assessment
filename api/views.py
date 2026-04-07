from django.views.decorators.csrf import csrf_exempt
from . import utils


@csrf_exempt
def get_or_add_user(request):
    if request.method == "POST":
        return utils.create_user(request)

    elif request.method == "GET":
        return utils.get_users(request)


@csrf_exempt
def update_or_delete_user(request, user_id):

    if request.method == "DELETE":
        return utils.delete_user(user_id)

    elif request.method in ["PUT", "PATCH"]:
        return utils.update_user(request, user_id)
