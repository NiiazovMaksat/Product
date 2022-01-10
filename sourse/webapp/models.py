from django.db import models

# Create your models here.
STATUS_CHOICES = [('other', 'Другое')]

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=STATUS_CHOICES, default='other')
    count = models.IntegerField(max_length=10, verbose_name="Остаток")
    price = models.DecimalField(max_length=10, verbose_name="Цена")