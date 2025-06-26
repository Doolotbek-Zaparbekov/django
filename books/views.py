from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.http import HttpResponse
from .models import Book, NewsBook

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book.html'
    ordering = ['-id']

class BookSearchListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains=query) if query else Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['average_rating'] = self.object.reviews.aggregate(avg_mark=Avg('mark'))['avg_mark']
        return context

class NewsBookCreateView(LoginRequiredMixin, CreateView):
    model = NewsBook
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AudioBookView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f"Вы запросили аудиозапись для книги с ID: {kwargs['book_id']}")

class StaticBookView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(
            '«Я лежал, кутаясь в свой краешек одеяла... Дом в котором...»')