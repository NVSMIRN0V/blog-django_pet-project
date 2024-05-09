from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from posts.models import Post, User, Like


def add_like(request, pk):
    post_id = pk
    user = request.user
    post = Post.objects.get(id=post_id)

    try:
        like = Like.objects.get(user=user, post=post)
        like.is_like = not like.is_like
        like.save()
    except Like.DoesNotExist:
        Like.objects.create(user=user, post=post, is_like=True)
    return redirect('detail', pk=post_id)


class DetailPostView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Где я?'
        return context
    

class PostsListView(ListView):
    model = Post
    template_name = 'posts/index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user.username)
            queryset = Post.objects.filter(author_id=user.pk)
        else:
            queryset = Post.objects.all()
        return queryset
            


class CreatePostView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.author = self.request.user
        return super().form_valid(form)


def detail_post(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Пост'})


def post_list(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Все посты'})
