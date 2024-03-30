import datetime

from rest_framework import views, response

from .serializers import FileSerializer
from .models import File, FileType

from web_vard.permissions import OnlyStaff, PerCustom


class ShowListFileAPIView(views.APIView):

    permission_classes = [OnlyStaff, ]

    def get(self, request):

        instance = File.objects.all()

        return response.Response({'List files': FileSerializer(instance, many=True).data})


class FileAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    @staticmethod
    def handle_uploaded_file(f):
        with open(f'file/media/{f.name}', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def get(self, request, **kwargs):

        if kwargs.get('my_files') != 'my_files':
            return response.Response({'Error': 'Data not defined'})

        instance = File.objects.filter(user_id=request.user.pk, date_delete=None)

        return response.Response({'Your data': FileSerializer(instance, many=True).data})

    def post(self, request, **kwargs):

        if kwargs.get('my_files') != 'my_files':
            return response.Response({'Error': 'Data not defined'})

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        request.data['user'] = 1

        if request.data.get('forms'):
            name_file = f'file/media/{request.data["name"]}_{File.objects.all().count() + 1}'
            extension_file = f'{FileType.objects.get(id=request.data["type"]).files_type.lower()}'

            with open(f'{name_file}.{extension_file}', 'w+') as file:
                file.write(request.data['forms'])

            request.data['link'] = f'{name_file}.{extension_file}'

        if request.FILES:
            self.handle_uploaded_file(request.FILES['link1'])
            request.data['link'] = f'file/media/{request.FILES["link1"].name}'

        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'File created': serializer.data})


class PutDeleteAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    def get(self, request, **kwargs):

        my_files = kwargs.get('my_files')
        pk = kwargs.get('pk')
        instance = File.objects.filter(user_id=request.user.pk).values('pk')

        if my_files != 'my_files' or {'pk': pk} not in instance:
            return response.Response({'Error': 'Data not defined'})

        instance = File.objects.get(pk=pk)

        if instance.date_delete:
            return response.Response({'Error': 'Data was deleted'})

        return response.Response({f'Data': FileSerializer(instance).data})

    def put(self, request, *args, **kwargs):

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        my_files = kwargs.get('my_files')
        pk = kwargs.get('pk')
        instance = File.objects.filter(user_id=request.user.pk).values('pk')

        if my_files != 'my_files' or {'pk': pk} not in instance:
            return response.Response({'Error': 'Data nor defined'})

        instance = File.objects.get(pk=pk)

        if request.data:
            instance.date_change = datetime.datetime.now()

        serializer = FileSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, *args, **kwargs):

        my_files = kwargs.get('my_files')
        pk = kwargs.get('pk')
        instance = File.objects.filter(user_id=request.user.pk).values('pk')

        if my_files != 'my_files' or {'pk': pk} not in instance:
            return response.Response({'Error': 'Data nor defined'})

        instance = File.objects.get(pk=pk)
        instance.date_delete = datetime.datetime.now()
        instance.save()

        return response.Response({'Data delete': f'Data <{pk}> was deleted'})
