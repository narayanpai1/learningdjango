from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    # 1 if veg,0 if non-veg
    veg = models.IntegerField(default=1)

    def __str__(self):
        return self.name