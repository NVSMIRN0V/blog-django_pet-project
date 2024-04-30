from django.urls import path
from posts.views import create_post, detail_post, home, post_list


urlpatterns = [
    path('', home, name='home'),
    path('create/', create_post, name='create'),
    path('detail/', detail_post, name='detail'),
    path('posts/', post_list, name='posts'),
]