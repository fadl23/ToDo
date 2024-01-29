from rest_framework import generics ,filters
from rest_framework import permissions
from .pagination import  TodoList_LO,Product_PN
from ..models import Todo,Productivity
from .serializers import ToDoSer ,ProductSer



class TodoList(generics.ListCreateAPIView):
    queryset= Todo.objects.all()
    serializer_class= ToDoSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = TodoList_LO
    filter_backends = [filters.SearchFilter]
    search_fields = ['task']

class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserTodo(generics.ListCreateAPIView):

    serializer_class= ToDoSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    def get_queryset(self):
        username = self.kwargs['username']
        return Todo.objects.filter(user__username=username)

class ProductivityList(generics.ListCreateAPIView):
    queryset= Productivity.objects.all()
    serializer_class= ProductSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Product_PN
    filter_backends = [filters.SearchFilter]
    search_fields = ['rating']


class ProductivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productivity.objects.all()
    serializer_class = ProductSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'





