from django.urls import path
from posts.views import CreatePostView, LikePostView, PostsListView, post_list


urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('detail/<int:pk>/', LikePostView.as_view(), name='detail'),
    path('posts/', post_list, name='posts'),
]