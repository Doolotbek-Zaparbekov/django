from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def book_list_view(request):
  if request.method == 'GET':
    book_list = models.Book.objects.all().order_by('-id')
    context = {
      'book_list': book_list
    }
    return render(request, template_name='book.html', context=context  )
  
  def book_detail_view(request, id):
    if request.method == 'GET':
      book_id = get_object_or_404(models.Book, id=id)
      context = {
        'book_id': book_id,
      }
      return render(request, template_name='book_detail.html', context=context)

def books(request):
  if request.method == 'GET':
    return HttpResponse('«Я лежал, кутаясь в свой краешек одеяла, и мне было хорошо. Я стал частью чего-то большого, многоногого и многорукого, теплого и болтливого. Я стал хвостом или рукой, а может быть даже костью. При каждом движении кружилась голова, и все равно давно уже мне не было так уютно.» Дом в котором...')
