from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from posts.models import Post



def home(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Главная'})


class CreatePostView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        # self.object = form.save()
        form.instance.author = self.request.user
        return super().form_valid(form)


def detail_post(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Пост'})


def post_list(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Все посты'})
