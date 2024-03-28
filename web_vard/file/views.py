import datetime

from rest_framework import views, response

from .serializers import FileSerializer
from .models import File


class GetPostFileAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instanse = File.objects.all()
            return response.Response({'List Files': FileSerializer(instanse, many=True).data})

        try:
            instance = File.objects.get(id=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        return response.Response({'Detail': FileSerializer(instance).data})

    def post(self, request):

        request.data['user'] = request.user.pk

        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'File created': serializer.data})


class PutDeleteAPIView(views.APIView):
    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        try:
            instance = File.objects.get(id=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        if request.data:
            instance.date_change = datetime.datetime.now()

        serializer = FileSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        try:
            instance = File.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.date_delete = datetime.datetime.now()
        instance.save()

        return response.Response({'Data delete': f'Запись {pk} удалена'})
