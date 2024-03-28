import datetime

from rest_framework import views, response


from .models import User
from .serializers import UserSerializer


class ShowListUserAPIView(views.APIView):
    def get(self, request):

        instance = User.objects.all()

        serializer = UserSerializer(instance, many=True)

        return response.Response({'List users': serializer.data})


class GetUserAPIView(views.APIView):
    def get(self, request, **kwargs):
        return response.Response({request.user.name: request.user})


class PostUserAPIView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(date=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'User created': serializer.data})


class PutDeleteUserAPIView(views.APIView):
    def put(self, request, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
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

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': f'Key - {pk} not defined'})

        request.user.delete()

        return response.Response({'Data delete': f'Data <{pk}> was deleted'})