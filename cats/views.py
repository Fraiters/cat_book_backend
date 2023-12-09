from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Cats
from .permissions import IsOwnerOrAdmin
from .serializer import CatsSerializer


class CatsApiList(ListAPIView):
    """ Просмотр списка всех котов """
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer


class CatsApiRetrieve(RetrieveAPIView):
    """ Просмотр одного кота """
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer


class CatsApiCreate(CreateAPIView):
    """ Добавление кота """
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes = (IsAuthenticated, )


class CatsApiUpdate(RetrieveUpdateAPIView):
    """ Просмотр и изменение кота """
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes = (IsOwnerOrAdmin, )


class CatsApiDestroy(DestroyAPIView):
    """ Удаление кота """
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes = (IsOwnerOrAdmin, )
