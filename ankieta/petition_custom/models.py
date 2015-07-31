from django.db import models
from petition.models import AbstractPetition, AbstractSignature
from django.utils.translation import ugettext_lazy as _
import swapper


class Petition(AbstractPetition):
    small_title = models.CharField(max_length=250, blank=True)
    text_top = models.TextField(blank=True)
    text_bottom = models.TextField(blank=True)
    text_read = models.TextField(blank=True)

    def __unicode__(self):
        return self.small_title

    class Meta:
        swappable = swapper.swappable_setting('petition', 'Petition')


class Signature(AbstractSignature):
    organization = models.CharField(max_length=100, blank=True, verbose_name=_("Organization"))
    newsletter = models.BooleanField(default=True, verbose_name=_("Newsletter acceptation"))

    class Meta:
        swappable = swapper.swappable_setting('petition', 'Signature')
