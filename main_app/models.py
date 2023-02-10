from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#first model-set name,time,rak'ah, gilat direction
class Prayers(models.Model):
    name: models.CharField(max_length=50)
    time: models.CharField(max_length=5)
    rakah: models.CharField(max_length=20)
    giblat_direction:models.CharField(max_length=10)

    def __str__(self):
        return f' {self.name.time.rakah}'
    
    def get_absolute_url(self):
        return reverse('tours_detail', kwargs={'pk': self.id})
    

class Salat(models.Model):
    name: models.CharField(max_length=20)
    time:models.CharField(max_length=20)
    rakah:models.CharField(max_length=50)
    giblat:models.CharField(max_length=10)


    def __str__(self):
        return f'{self.name.time.rakak.giblat}, {self.time.rakah}'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'salat_id': self.id})
    

   