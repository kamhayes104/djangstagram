from unicodedata import name
from django.urls import path
from .views import home_view, post_view, post_detail_view, create_post_view


urlpatterns = [
    path('', home_view, name='home_view'),
    path('posts', post_view, name='post_view'),
    path('post/<int:pk>', post_detail_view, name='post_detail_view'),
    path('post/create', create_post_view, name='create_post_view')
]
