from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models

from django.urls import reverse
from django.utils.translation import gettext_lazy as _



class CustomUser(AbstractUser):

    address1 = models.CharField(verbose_name=_("Address line 1"), max_length=1024, blank=True, null=True)
    address2 = models.CharField(verbose_name=_("Address line 2"), default="None", max_length=1024, blank=True,
                                null=True)
    zip_code = models.CharField(verbose_name=_("Postal code"), max_length=149, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=1024, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True, default="None")

    mobile_phone = models.CharField(verbose_name=_("Mobile phone"), max_length=100, blank=True, null=True)



    recharged_amount = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    # site = models.ForeignKey(Site, default=2,  on_delete=models.CASCADE ,related_name='site')

    def __str__(self):
        return str(self.username)
