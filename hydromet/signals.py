__author__ = 'jbjeanniton'

from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from hydromet.models import Observation

@receiver(post_save, sender=Observation)
def model_post_save(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))
