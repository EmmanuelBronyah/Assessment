from django.http.response import JsonResponse
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def users(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if not data:
            return JsonResponse({"message": "Invalid data"}, status=400)

        name = data.get("name")
        role = data.get("role")

        if not name or not role:
            return JsonResponse({"message": "name and role are required"}, status=400)

        user = User.objects.create(name=name, role=role)

        return JsonResponse(
            {"id": user.id, "name": user.name, "role": user.role}, status=201
        )

    elif request.method == "GET":
        role = request.GET.get("role")

        if not role:
            return JsonResponse(
                {"message": "role query parameter is required"}, status=400
            )

        if role == "all":
            users = list(User.objects.values())
        else:
            users = list(User.objects.filter(role=role).values())

        return JsonResponse(users, safe=False)
