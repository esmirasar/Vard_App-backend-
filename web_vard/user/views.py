import datetime

from django.contrib.auth import logout

from rest_framework import views, response
from rest_framework.decorators import api_view

from web_vard.permissions import UserPerCustom, OnlyStaff

from .models import User, Token
from .serializers import UserSerializer, TokenSerializer
from .constant import RANDOM_STRING


class ShowListUserAPIView(views.APIView):

    permission_classes = [OnlyStaff, ]

    def get(self, request):

        instance = User.objects.all()

        serializer = UserSerializer(instance, many=True)

        return response.Response({'List users': serializer.data})


class PostUserAPIView(views.APIView):
    def get(self, request):

        user = request.user

        if not request.user.id:
            return response.Response({'Enter your data': 'AnonymousUser'})

        logout(request)

        return response.Response({'Logged out': user.name})

    def post(self, request):

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        if len(request.data) > 3:
            return response.Response({'Error': 'More than 3 fields'})

        if not request.data.get('username'):
            return response.Response({'Error': 'Enter username'})

        if not request.data.get('email'):
            return response.Response({'Error': 'Enter email'})

        if not request.data.get('password'):
            return response.Response({'Error': 'Enter password'})

        request.data['token'] = RANDOM_STRING
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Success': 'Check email'})


@api_view(('POST', ))
def accept_registration(request, **kwargs):
    try:
        data = Token.objects.get(token=kwargs['token'])
    except:
        return response.Response({'Error': '404'})

    token_serializer = TokenSerializer(data).data
    user_serializer = UserSerializer(data=token_serializer)
    user_serializer.is_valid(raise_exception=True)
    user_serializer.save()
    data.delete()
    return response.Response({'Success': "User registered"})


class GetPutDeleteUserAPIView(views.APIView):

    permission_classes = [UserPerCustom, ]

    def get(self, request, **kwargs):

        if kwargs.get('my_profile') != 'my_profile':
            return response.Response({'Error': 'Not data'})

        instance = UserSerializer(request.user)

        return response.Response({request.user.name: instance.data})

    def put(self, request, **kwargs):

        pk = kwargs.get('my_profile')

        if pk != 'my_profile':
            return response.Response({'Error': f'Key - {pk} not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        instance = request.user

        if request.data.get('password'):
            instance.date_password.change = datetime.datetime.now()

        serializer = UserSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, **kwargs):

        data_user = request.user

        pk = kwargs.get('my_profile')

        if pk != 'my_profile':
            return response.Response({'Error': f'Key - {pk} not defined'})

        request.user.delete()

        return response.Response({'Data delete': f'Data <{data_user.email}> was deleted'})
