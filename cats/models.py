from django.contrib.auth.models import User
from django.db.models import Model, IntegerField, CharField, TextField, ImageField, ForeignKey, CASCADE


class Cats(Model):
    """ Модель Кот """
    class Meta:
        verbose_name = 'Кот'

    name = CharField(max_length=100, verbose_name="Имя")
    age = IntegerField(null=True, verbose_name="Возраст")
    breed = CharField(max_length=100, blank=True, verbose_name="Порода")
    weight = IntegerField(null=True, verbose_name="Вес")
    photo = ImageField(upload_to="photos/", blank=True, verbose_name="Фото")
    description = TextField(blank=True, verbose_name="Описание")
    author = ForeignKey(User, verbose_name='Пользователь', on_delete=CASCADE)

    def __str__(self):
        return self.name
