from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Relocation


@receiver(post_save, sender=Relocation)
def create_tasks(sender, instance, created, **kwargs):

    if created:
        instance.create_default_tasks()