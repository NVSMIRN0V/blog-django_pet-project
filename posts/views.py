from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


from posts.models import Post
from users.models import User


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
    success_url = reverse_lazy('signin')

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
