from django.db import models


class Category(models.Model):

    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    CHOICE_STATUS = (
        (STATUS_INACTIVE, 'inactivo'),
        (STATUS_ACTIVE, 'activo')
    )

    name = models.CharField(
        max_length=30
    )

    status = models.SmallIntegerField(
        choices=CHOICE_STATUS,
        default=STATUS_INACTIVE
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    class Meta:
        app_label = 'cat'
