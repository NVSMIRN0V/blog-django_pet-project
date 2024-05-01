from django.urls import path
from posts.views import CreatePostView, PostsListView, detail_post, post_list


urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('detail/', detail_post, name='detail'),
    path('posts/', post_list, name='posts'),
]