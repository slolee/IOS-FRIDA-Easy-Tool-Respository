from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('repositoryList', views.repositoryList),
    path('repositorySearch', views.repositorySearch),
    path('repositoryCheckName', views.repositoryCheckName),
    path('createRepository', views.createRepository),
    path('deleteRepository', views.deleteRepository),
    path('scriptBoardList/<id>', views.scriptBoardList),
    path('scriptBoardSearch', views.scriptBoardSearch),
    path('postCheckName', views.postCheckName),
    path('createPost', views.createPost),
    path('getPost', views.getPost),
    path('getRepository', views.getRepository),
    path('getRepositoryId', views.getRepositoryId),
    path('getRepositoryList', views.getRepositoryList),
    path('deletePost', views.deletePost),
]
