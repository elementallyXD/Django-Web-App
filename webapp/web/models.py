from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    ROLE_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
