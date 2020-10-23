from apps.products.models import Option
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_admin = self.is_admin or self.can_edit
        super(User, self).save(*args, **kwargs)

    def take(self, option):
        if not option.can_be_taken():
            return False
        taken = UserProduct(user=self, option=option)
        taken.save()
        option.stock = option.stock - 1
        option.save()
        return True


class UserProduct(models.Model):
    user = models.ForeignKey(
        User, related_name='+',
        verbose_name=_("User"), on_delete=models.CASCADE)
    option = models.ForeignKey(
        Option, related_name='+',
        verbose_name=_("Option"), on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}:{}'.format(self.user, self.option.product, self.option)
