from django.db import models


class Distinction(models.TextChoices):
    AVERAGE = 'average'
    RESPECTED = 'respected'
    INAPPROPIATE = 'inappropiate'
    DESPICABLE = 'despicable'
    HATEFUL = 'hateful'
    