from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'
    