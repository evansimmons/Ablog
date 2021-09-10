#b_log/urls.py
from django.urls import path, include
from .views import BlogDetailView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(),
            name='post_detail'),
]
