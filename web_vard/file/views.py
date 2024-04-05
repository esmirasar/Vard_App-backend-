import datetime

from rest_framework import views, response

from .serializers import FileSerializer
from comment.serializers import CommentSerializer
from .models import File, FileType
from comment.models import Comment

from web_vard.permissions import OnlyStaff, PerCustom


class ShowListFileAPIView(views.APIView):

    permission_classes = [OnlyStaff, ]

    def get(self, request):

        instance = File.objects.all()

        return response.Response({'List files': FileSerializer(instance, many=True).data})


class FileAPIView(views.APIView):

    # permission_classes = [PerCustom, ]

    @staticmethod
    def handle_uploaded_file(f):
        with open(f'file/media/{f.name}', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def get(self, request, **kwargs):

        if kwargs.get('my_files') != 'my_files':
            return response.Response({'Error': 'Data not defined'})

        instance = File.objects.filter(user_id=request.user.pk, date_delete=None)
        instance_comment = Comment.objects.filter(user_id=request.user.pk, date_remove=None)

        return response.Response({'Your files': FileSerializer(instance, many=True).data,
                                  'Your descriptions': CommentSerializer(instance_comment, many=True).data})

    def post(self, request, **kwargs):

        if kwargs.get('my_files') != 'my_files':
            return response.Response({'Error': 'Data not defined'})

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        request.data['user'] = 1

        if request.FILES:
            for i in request.FILES.getlist('link1'):
                self.handle_uploaded_file(i)
                request.data['link'] = f'file/media/{i.name}'
                serializer = FileSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

        return response.Response({'Success': 'data created'})


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

        instance_comment = Comment.objects.filter(file_id=pk)

        return response.Response({'Your file': FileSerializer(instance).data,
                                  'File description': CommentSerializer(instance_comment, many=True).data})

    def post(self, request, **kwargs):

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        my_files = kwargs.get('my_files')
        pk = kwargs.get('pk')
        instance = File.objects.filter(user_id=request.user.pk).values('pk')

        if my_files != 'my_files' or {'pk': pk} not in instance:
            return response.Response({'Error': 'Data nor defined'})

        request.data['user'] = request.user.pk
        request.data['date_send'] = datetime.datetime.now()
        request.data['date_delivery'] = datetime.datetime.now()
        request.data['file'] = pk

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Comment added': serializer.data})

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

        if request.data.get('description'):

            Comment.objects.create(user_id=request.user.pk, file_id=pk)
            instance_comment = Comment.objects.get(file_id=pk)
            instance_comment.comment = request.data['description']
            instance_comment.date_send = datetime.datetime.now()
            serializer_comment = CommentSerializer(data=request.data, instance=instance_comment, partial=True)
            serializer_comment.is_valid(raise_exception=True)
            serializer_comment.save()
            instance_comment.date_delivery = datetime.datetime.now()
            serializer_comment.save()

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
        instance_comment = Comment.objects.filter(file_id=pk)
        instance_comment.date_remove = instance.date_delete
        instance.save()
        instance_comment.save()

        return response.Response({'Data delete': f'Data <{pk}> was deleted'})

