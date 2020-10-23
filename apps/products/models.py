import uuid

from apps.events.models import Stand
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    stand = models.ForeignKey(
        Stand, related_name='products',
        verbose_name=_("Stand"), null=True, on_delete=models.SET_NULL)
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100, blank=False)
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True, help_text=_("a detailed description of the product"))

    def __str__(self):
        return self.name

    def get_options(self):
        return Option.objects.filter(product=self, stock__gt=0)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Option(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    product = models.ForeignKey(
        Product, related_name='options',
        verbose_name=_("Product"), on_delete=models.CASCADE)
    description = models.CharField(
        verbose_name=_("Description"),
        max_length=100, blank=False)
    stock = models.PositiveSmallIntegerField(
        blank=True, default=0)

    def __str__(self):
        return self.description

    def can_be_taken(self):
        return self.stock > 0

    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")
        ordering = ['product__name', 'description']
