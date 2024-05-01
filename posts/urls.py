from django.urls import path
from posts.views import CreatePostView, detail_post, home, post_list


urlpatterns = [
    path('', home, name='home'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('detail/', detail_post, name='detail'),
    path('posts/', post_list, name='posts'),
]