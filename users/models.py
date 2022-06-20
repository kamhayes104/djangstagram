from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(
        "self",  # profiles are followed by/follow other profiles
        related_name="followed_by", # allows relationship to be used in other contexts
        symmetrical=False, # users don't necessarily have to follow each other
        blank=True # profile doesn't have to follow anyone
    )
    picture = models.ImageField(upload_to='')
    bio = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        profile.following.add(instance.profile)
        profile.save()