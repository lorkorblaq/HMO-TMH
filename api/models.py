from django.db import models

# Create your models here.
class Hospitals(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    image = models.ImageField(upload_to='api/images/hosptials')
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
