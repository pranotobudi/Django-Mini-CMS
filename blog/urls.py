from django.urls import path, include
from . import views
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    post_load, 
                    UserPostListView
                )
urlpatterns = [
    # path('', views.Home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post-load/', post_load, name='post-load'),
    path('post/<str:username>/', UserPostListView.as_view(), name='post-user'),

    path('about/', views.About, name='blog-about'),
]
