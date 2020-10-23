import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100, blank=False)
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True, help_text=_("a detailed description of the event"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ['name']


class Stand(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    event = models.ForeignKey(
        Event, related_name='stands',
        verbose_name=_("Event"), on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Stand")
        verbose_name_plural = _("Stands")
        ordering = ['event__name', 'name']
