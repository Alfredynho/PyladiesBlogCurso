from django.urls import path

from .views import PostList, DetailPost

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
	path('post/detalle/<int:pk>/', DetailPost.as_view(),name='detail_post'),    
]