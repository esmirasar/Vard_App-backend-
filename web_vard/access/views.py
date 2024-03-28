from django.shortcuts import render
from rest_framework import views, response
from access.serializers import AccessSerializer
from access.models import Access
import datetime


class GetPostAccessAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instance = Access.objects.all()
            return response.Response({'Access list': AccessSerializer(instance, many=True).data})

        try:
            instance = Access.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        return response.Response({'Detail': AccessSerializer(instance).data})

    def post(self, request):

        request.data['user'] = request.user.pk

        serializer = AccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Access created': serializer.data})

class PutDeleteAccessAPIView(views.APIView):
    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        try:
            instance = Access.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        serializer = AccessSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Access update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        try:
            instance = Access.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.date_access_close = datetime.datetime.now()
        instance.save()

        return response.Response({'Access deleted': f'Запись {pk} удалена'})