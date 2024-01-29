from rest_framework import serializers
from ..models import Todo,Productivity

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Productivity
        fields ='__all__'
        depth= 10


class ToDoSer(serializers.ModelSerializer):
    productivity=ProductSer(many=True,read_only=True)

    class Meta:
        model = Todo
        fields ='__all__'




