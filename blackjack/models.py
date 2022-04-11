from django.db import models



class Object(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер')
    name = models.CharField(max_length=1000, verbose_name='Наименование')
    code = models.IntegerField(default=1, verbose_name='Код')
    inv = models.CharField(max_length=1000, verbose_name='Инвентарный номер')
    price = models.FloatField(verbose_name='Цена')
    count = models.IntegerField(verbose_name='Количество')
    summ = models.FloatField(verbose_name='Сумма')
    note = models.TextField(verbose_name='Примечание')















