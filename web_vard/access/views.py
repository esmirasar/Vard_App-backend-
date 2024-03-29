import datetime

from rest_framework import views, response

from web_vard.permissions import OnlyStaff, PerCustom

from .serializers import AccessSerializer
from .models import Access


class ListAccessAPIView(views.APIView):

    permission_classes = [OnlyStaff, ]

    def get(self, request):

        instance = Access.objects.all()

        return response.Response({'List data': AccessSerializer(instance, many=True).data})


class GetPostAccessAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    def get(self, request, *args, **kwargs):

        if kwargs.get('my_access') != 'my_access':
            return response.Response({'Error': 'Data not defined'})

        instance = Access.objects.filter(user_id=request.user.pk, date_access_close=None)

        return response.Response({'Detail': AccessSerializer(instance, many=True).data})

    def post(self, request, **kwargs):

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        if kwargs.get('my_access') != 'my_access':
            return response.Response({'Error': 'Data not defined'})

        request.data['user'] = request.user.pk

        serializer = AccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Access created': serializer.data})


class PutDeleteAccessAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    def get(self, request, **kwargs):

        my_access = kwargs.get('my_access')
        pk = kwargs.get('pk')
        instance = Access.objects.filter(user_id=request.user.pk).values('pk')

        if my_access != 'my_access' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Access.objects.get(pk=pk)

        if instance.date_access_close:
            return response.Response({'Data delete': f'Data <{pk}> was deleted'})

        return response.Response({'Data': AccessSerializer(instance).data})

    def put(self, request, *args, **kwargs):

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        my_access = kwargs.get('my_access')
        pk = kwargs.get('pk')
        instance = Access.objects.filter(user_id=request.user.pk).values('pk')

        if my_access != 'my_access' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Access.objects.get(pk=pk)

        instance.date_change = datetime.datetime.now()

        serializer = AccessSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, *args, **kwargs):

        my_access = kwargs.get('my_access')
        pk = kwargs.get('pk')
        instance = Access.objects.filter(user_id=request.user.pk).values('pk')

        if my_access != 'my_access' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Access.objects.get(pk=pk)

        instance.date_access_close = datetime.datetime.now()
        instance.save()

        return response.Response({'Access deleted': f'Запись {pk} удалена'})