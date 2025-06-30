from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Movie, Genre
from .forms import MovieForm, CommentForm, RegisterForm
from django.db.models import Q, Avg

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
class LoginUserView(LoginView):
    template_name = 'accounts/login.html'

class LogoutUserView(LogoutView):
    next_page = reverse_lazy('login')

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5
    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.GET.get('q')
        genre = self.request.GET.get('genre')
        sort = self.request.GET.get('sort')
        if query:
            queryset = queryset.filter(title__icontains=query)
        if genre:
            queryset = queryset.filter(genres__name__iexact=genre)
        if sort == 'rating':
            queryset = queryset.order_by('-rating')
        elif sort == 'date':
            queryset = queryset.order_by('-release_date')
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')
    def test_func(self):
        movie = self.get_object()
        return movie.author == self.request.user

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')
    def test_func(self):
        movie = self.get_object()
        return movie.author == self.request.user

class AddCommentView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    def form_valid(self, form):
        movie_id = self.kwargs['pk']
        form.instance.author = self.request.user
        form.instance.movie_id = movie_id
        form.save()
        return redirect('movie_detail', pk=movie_id)