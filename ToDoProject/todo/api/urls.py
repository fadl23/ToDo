from django.urls import path
from .views import TodoList,ToDoDetail,ProductivityList, ProductivityDetail ,UserTodo

urlpatterns = [
    path('TodoList/',TodoList.as_view(),name='Todo-List'),
    path('UserTodo/<str:username>/' ,UserTodo.as_view(),name='user-Todo-List'),
    path('ToDoDetail/<int:id>/',ToDoDetail.as_view(),name='ToDo-Detail'),
    path('ProductList/',ProductivityList.as_view(),name='Product-List'),
    path('ProctDetail/<int:id>',ProductivityDetail.as_view(),name='Product-Detail'),

]