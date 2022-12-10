from pickle import TRUE
from django.db import models
class diseases(models.Model):
    Name=models.CharField(max_length=100)
    x_ray=models.TextField()
    ct=models.TextField(blank=TRUE, null=TRUE)
    vc=models.CharField(blank=TRUE, null=TRUE,max_length=100)
    fev=models.CharField(blank=TRUE, null=TRUE,max_length=100)
    ratio=models.CharField(blank=TRUE, null=TRUE,max_length=100)
    tlc=models.CharField(blank=TRUE, null=TRUE,max_length=100)
    rv=models.CharField(blank=TRUE, null=TRUE,max_length=100)
    physical=models.TextField(blank=TRUE, null=TRUE)
    others=models.TextField(blank=TRUE, null=TRUE)
    def __str__(self):
        return self.Name

class pred(models.Model):
    img=models.ImageField(upload_to='pred/%y/%m/%d')
    name= models.CharField(blank=TRUE, null=TRUE,max_length=100)
