from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postImage', views.postImage, name="postsubmit"),
    path('search', views.search, name="search")
] 