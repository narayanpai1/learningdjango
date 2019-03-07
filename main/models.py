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


class nc_comments(models.Model):
    nc=models.ForeignKey(nc,on_delete=models.CASCADE)
    value=models.TextField()
    likes=models.IntegerField()

    def __str__(self):
        return self.nc.name + '-' + self.value[:10]+ "..."


class comment_on_comment(models.Model):
    parent=models.ForeignKey(nc_comments,on_delete=models.CASCADE)
    value=models.TextField()
    likes=models.IntegerField()

    def __str__(self):
        return self.value[:10]+ "..."


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

    def __str__(self):
        return self.name


class current_items(models.Model):
    items=models.ForeignKey(dishes,on_delete=models.CASCADE)


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