import datetime

from rest_framework import views, response

from .serializers import CommentSerializer, ReadCommentSerializer
from .models import Comment, ReadComment


class GetPostCommentAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instance = Comment.objects.all()
            return response.Response({'list comments': CommentSerializer(instance, many=True).data})

        try:
            instance = Comment.objects.get(pk=pk)
        except:
            return response.Response({'Error': 'data not defined'})

        return response.Response({'Detail': CommentSerializer(instance).data})

    def post(self, request):

        request.data['user'] = request.user.pk

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Comment created': serializer.data})


class DeletePutCommentAPIView(views.APIView):
    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        try:
            instance = Comment.object.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        serializer = CommentSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        try:
            instance = Comment.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.date_remove = datetime.datetime.now()
        instance.save()

        return response.Response({'Data deleted': f'Комментарий под номером {pk} удален'})


class ReadCommentAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instance = ReadComment.objects.all()
            return response.Response({'list readcomment': ReadCommentSerializer(instance, many=True).data})

        try:
            instance = ReadComment.objects.get(pk=pk)
        except:
            return response.Response({'Error': 'data not defined'})

        return response.Response({'Detail': ReadCommentSerializer(instance).data})

    def post(self, request):

        request.data['user'] = request.user.pk

        serializer = ReadCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Read comment created': serializer.data})

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        try:
            instance = ReadComment.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        serializer = ReadCommentSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Read comment update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        try:
            instance = ReadComment.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.delete()

        return response.Response({'Read comment deleted': f'Запись {pk} удалена'})