from django.urls import path
from blog import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts, name='posts'),
    path('posts/<slug:slug>', views.post_detail, name= 'post-detail') #/posts/my-first-post
]
