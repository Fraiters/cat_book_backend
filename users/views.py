from rest_framework.authtoken.admin import User
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class UserByTokenApi(APIView):
    """ Просмотр информации о пользователе по токену """

    def get(self, request):
        data = {
            "id": str(request.user.id),
            "username": str(request.user.username)
        }
        return Response(data)
