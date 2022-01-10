from django.db import models

# Create your models here.
STATUS_CHOICES = [('other', 'Другое')]

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    category = models.CharField(max_length=100, null=False, verbose_name="Категория", choices=STATUS_CHOICES, default='other')
    count = models.IntegerField(max_length=10, verbose_name="Остаток")
    price = models.DecimalField(decimal_places=2, max_digits=9, max_length=10, verbose_name="Цена")

    def __str__(self):
        return f'{self.pk}) {self.name} : {self.category} / {self.count} | {self.price}'

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
