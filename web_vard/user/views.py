import datetime

from django.contrib.auth import logout

from rest_framework import views, response

from web_vard.permissions import UserPerCustom, OnlyStaff

from .models import User
from .serializers import UserSerializer


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

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'User created': serializer.data})


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
