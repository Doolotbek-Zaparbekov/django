from django.db import models
from django.core.validators import MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Обложка книги')
    description = models.TextField(verbose_name='Описание')
    TYPE_BOOK = (
        ('Magic realism', 'Magic realism'),
        ('Novel', 'Novel'),
        ('Fantasy', 'Fantasy')
    )
    type_book = models.CharField(max_length=20, choices=TYPE_BOOK, verbose_name='Тип книги')

    def __str__(self):
        return self.title

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
