from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя клиента')
    organisation = models.TextField(verbose_name='Название организации')
    number_of_account = models.PositiveIntegerField(verbose_name='Номер счета')
    sum = models.FloatField(verbose_name='Сумма')
    service = models.TextField(verbose_name='Справочник')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        db_table = 'Account'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        unique_together = ['name', 'number_of_account', 'organisation']

    def __str__(self):
        return
