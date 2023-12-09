from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, CurrentUserDefault

from .models import Cats


class CatsSerializer(ModelSerializer):
    """ Сериализатор кота """
    author = CharField(default=CurrentUserDefault())

    class Meta:
        model = Cats
        fields = "__all__"
