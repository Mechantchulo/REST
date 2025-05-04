from django.urls import path

from .views import ListTodo, DetailTodo

#create a list of urls

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()), #detailview
    path('', ListTodo.as_view()), #listview
]