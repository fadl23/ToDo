from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegisterSerializer
from .. import models


@api_view(['POST,'])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delate()
        return Response(status=status.HTTP_200_OK)








@api_view(['POST,'])

def register_view(request):



    if request.method == 'POST':
        serializer= RegisterSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account=serializer.save()

            data['response'] ='Regestaration Successfull'
            data['username'] = account.username
            data['email'] = account.email
            token=Token.objects.get(user=account).key
            data['token'] = token
        else:
            data= serializer.errors

        return Response(serializer.data)