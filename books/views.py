from django.shortcuts import render
from django.http import HttpResponse

def books(request):
  if request.method == 'GET':
    return HttpResponse('«Я лежал, кутаясь в свой краешек одеяла, и мне было хорошо. Я стал частью чего-то большого, многоногого и многорукого, теплого и болтливого. Я стал хвостом или рукой, а может быть даже костью. При каждом движении кружилась голова, и все равно давно уже мне не было так уютно.» Дом в котором...')
