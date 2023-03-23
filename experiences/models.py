from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    name = models.CharField(max_length=250, default="")
    country = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=80, default="")
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    price = models.IntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()

    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(max_length=100)
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanations = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name