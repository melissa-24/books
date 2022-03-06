from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Author)
def create_writer(sender, instance, created, **kwargs):
    if created:
        Writer.objects.create(author=instance)

@receiver(post_save, sender=Book)
def create_story(sender, instance, created, **kwargs):
    if created:
        Story.objects.create(book=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Author)
def save_writer(sender, instance, **kwargs):
    instance.writer.save()

@receiver(post_save, sender=Book)
def save_story(sender, instance, **kwargs):
    instance.story.save()