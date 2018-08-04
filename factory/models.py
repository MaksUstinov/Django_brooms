from django.db import models

# Create your models here.
class Factory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    production = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    cities = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}'.format(self.name)


class City(models.Model):
    name = models.CharField(max_length=100)
    suppliers = models.TextField()

    def __str__(self):
        return '%s' % (self.name)