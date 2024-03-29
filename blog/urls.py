from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
finalDataListCommon,
finalDataListPopular,
finalDataListBoth,
)
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('data/common', finalDataListCommon.as_view(), name='finalDataListCommon'),
    path('data/popular', finalDataListPopular.as_view(), name='finalDataListPopular'),
    path('data/both', finalDataListBoth.as_view(), name='finalDataListBoth'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
