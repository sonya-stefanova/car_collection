from car_collection.web.validators import CustomMinLengthValidator, YearValidator
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(
                2,
                "The username must be a minimum of 2 chars"
            )
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank = False,
        null = False,
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(18)
        ],
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=30,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    TYPES = (
        ("Sport Car", "Sport Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    type = models.CharField(
        max_length=9,
        choices=TYPES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=20,
    )

    year = models.IntegerField(
        validators=[
            YearValidator(1980, 2049),
        ],
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1),

        ]
    )

    def __str__(self):
        return f'{self.type} -> {self.model}'