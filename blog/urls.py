from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.index, name='blog-index'),
    path('', PostListView.as_view(), name='blog-index'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post-detail'),
    path('post/new/', PostCreateView.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-post-delete'),
    path('about/', views.about, name='blog-about'),
]
