from django.db import models


class Product(models.Model):

    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    CHOICE_STATUS = (
        (STATUS_INACTIVE, 'inactivo'),
        (STATUS_ACTIVE, 'activo')
    )

    category = models.ManyToManyField(
        'Category',
        related_name='product_set',
        null=True
    )

    name = models.CharField(
        max_length=30
    )

    description = models.TextField(
        max_length=150
    )


    image = models.CharField(
        max_length=80
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