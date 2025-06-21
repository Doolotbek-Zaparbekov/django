from django.db import models
from django.core.validators import MaxValueValidator
from books.models import Book

class Basket(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Подтвержден'),
        ('not_confirmed', 'Не подтвержден'),
    )

    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    card_number = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999999999999999)],
        verbose_name='Номер карты'
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_confirmed')

    def __str__(self):
        return f"{self.full_name} - {self.book.title}"
