from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите картинку')
    description = models.TextField(verbose_name='Дайте описание')
    TYPE_BOOK =(
        ('Magic realism', 'Magic realism'),
        ('Novel', 'Novel'),
        ('Fantasy', 'Fantasy')
    )
    type_book = models.CharField(max_length=100, choices=TYPE_BOOK)
    link_youtube = models.URLField(verbose_name='вставте ссылку', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'
    
class Reviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True, verbose_name='Книга')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    text = models.TextField(verbose_name='Напишите отзыв')
    mark = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Оценка должна быть не меньше 1."),
            MaxValueValidator(5, message="Оценка должна быть не больше 5.")
        ],
        verbose_name='Оценка от 1 до 5',
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book} - {self.author} - {self.mark}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class NewsBook(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='Автор'
        verbose_name_plural ='Автор'