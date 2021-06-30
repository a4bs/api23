from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Informatiomuser(models.Model):
    user=models.ForeignKey(User,related_name='posting',on_delete=models.CASCADE)
    infromation=models.BooleanField(default=True)
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phone=models.CharField(max_length=30,null=True)
    nameworke=models.CharField(max_length=30)
    nameinstgran=models.CharField(max_length=30)
    image=models.ImageField(upload_to='./media/user/')
    Date = models.DateField(null=True, blank=True)
class postinf(models.Model):
    byuser=models.ForeignKey(User,on_delete=models.CASCADE)
    imag=models.ImageField(upload_to='./media/posting/')
class postincordenent(models.Model):
    user=models.ForeignKey(User,related_name='posation',on_delete=models.CASCADE)
    lattude=models.CharField(max_length=255)
    longtude=models.CharField(max_length=255)