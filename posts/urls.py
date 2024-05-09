from django.urls import path
from posts.views import CreatePostView, DetailPostView, PostsListView, add_like, post_list


urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailPostView.as_view(), name='detail'),
    path('detail/<int:pk>/like/', add_like, name='like'),
    path('posts/', post_list, name='posts'),
]