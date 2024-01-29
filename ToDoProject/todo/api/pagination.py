from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination


class TodoList_LO(LimitOffsetPagination):
    default_limit= 2
    limit_query_param= 'l'
    offset_query_param= 'o'
    max_limit= 2

class Product_PN(PageNumberPagination):
    page_size=2
    page_query_param='p'
    page_size_query_param='size'
    max_page_size=4
