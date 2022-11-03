from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'