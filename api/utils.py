from django.http.response import JsonResponse
import json
from .models import User


def validate_role(role):
    if role not in ["admin", "vendor", "customer"]:
        return JsonResponse({"message": "Invalid role"}, status=400)


def check_name_is_empty(name):
    if not name:
        return JsonResponse({"message": "name is required"}, status=400)


def check_role_is_empty(role):
    if not role:
        return JsonResponse({"message": "role is required"}, status=400)


def create_user(request):
    data = json.loads(request.body)

    if not data:
        return JsonResponse({"message": "Invalid data"}, status=400)

    name = data.get("name")
    role = data.get("role")

    error = check_name_is_empty(name)
    if error:
        return error

    error = check_role_is_empty(role)
    if error:
        return error

    error = validate_role(role)
    if error:
        return error

    user = User.objects.create(name=name, role=role)

    return JsonResponse(
        {"id": user.id, "name": user.name, "role": user.role}, status=201
    )


def get_users(request):
    role = request.GET.get("role")

    error = check_role_is_empty(role)
    if error:
        return error

    if role == "all":
        users = list(User.objects.values())
    else:
        users = list(User.objects.filter(role=role).values())

    return JsonResponse(users, safe=False)


def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    user.delete()
    return JsonResponse({"message": "User deleted successfully"})


def update_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    data = json.loads(request.body)

    if "name" in data:
        error = check_name_is_empty(data["name"])
        if error:
            return error

        user.name = data["name"]

    if "role" in data:
        error = check_role_is_empty(data["role"])
        if error:
            return error

        error = validate_role(data["role"])
        if error:
            return error

        user.role = data["role"]

    user.save()

    return JsonResponse({"id": user.id, "name": user.name, "role": user.role})
