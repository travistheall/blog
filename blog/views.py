from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Mostcommon, Mostpopular, Both


def home(request):
    context = {
        'blog': 'blog',
    }
    return render(request, 'blog/blogPost.html', context)


class finalDataListCommon(ListView):
    paginate_by = 10
    template_name = 'blog/dataCommon.html'
    context_object_name = 'mostCommon'
    model = Mostcommon
    ordering = ['neigh']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Data'] = 'Data'
        context['Common'] = 'Common'
        context['links'] = ['Final', 'Data']
        return context


class finalDataListPopular(ListView):
    paginate_by = 10
    template_name = 'blog/dataPopular.html'
    context_object_name = 'mostPopular'
    model = Mostpopular
    ordering = ['neigh']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Data'] = 'Data'
        context['Popular'] = 'Popular'
        context['links'] = ['Final', 'Data']
        return context


class finalDataListBoth(ListView):
    paginate_by = 10
    template_name = 'blog/dataBoth.html'
    context_object_name = 'both'
    model = Both

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Data'] = 'Data'
        context['Both'] = 'Both'
        context['links'] = ['Final', 'Data']
        return context



def old_home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)
