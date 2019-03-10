from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class nc(models.Model):
    name=models.CharField(max_length=50)
    phno=models.BigIntegerField()

    def __str__(self):
        return self.name


class filter(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class dishes(models.Model):
    nc=models.ForeignKey(nc,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    filter=models.ForeignKey(filter,on_delete=models.CASCADE,default=1)
    veg = models.BooleanField(default=True)
    currently_present=models.BooleanField()


    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ncnumber=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()