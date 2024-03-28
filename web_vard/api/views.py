import datetime

from rest_framework import views, response, generics

from .serializers import (UserSerializer, FileSerializer, AccessSerializer, FeedbackSerializer,
                          ChartSerializer, DashboardSerializer, CommentSerializer, ReadCommentSerializer)

from models.models import (User, File,  Access, Feedback,
                           Chart, Dashboard, Comment, ReadComment)

from .permissions import ReadOnDeleteAd


class UserAPIView(views.APIView):
    permission_classes = (ReadOnDeleteAd, )

    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instance = User.objects.all().values()
            return response.Response({'List users': UserSerializer(instance, many=True).data})

        try:
            instance = User.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        return response.Response({'Detail': UserSerializer(instance).data})

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'User created': serializer.data})

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data fot change'})

        try:
            instance = User.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        if request.data.get('password'):
            instance.date_passwords_change = datetime.datetime.now()


        serializer = UserSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        try:
            instance = User.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.delete()

        return response.Response({'Data delete': f'Запись {pk} удалена'})


class FileAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get("pk")

        if not pk:
            instance = File.objects.all()
            return response.Response({"List Files": FileSerializer(instance, many=True).data})

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


class DashboardAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instance = Dashboard.objects.all()
            return response.Response({'List dashboards': DashboardSerializer(instance, many=True).data})

        try:
            instance = Dashboard.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        return response.Response({'Detail': DashboardSerializer(instance).data})

    def post(self, request):

        request.data['user'] = request.user.pk
        serializer = DashboardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Dashboard created': serializer.data})

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        try:
            instance = Dashboard.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        if request.data:
            instance.date_change = datetime.datetime.now()

        serializer = DashboardSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': "PK not defined"})

        try:
            instance = Dashboard.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.delete()

        return response.Response({'Data deleted': f'Запись под номером {pk} удалена'})


class CommentAPIView(views.APIView):
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


class AccessAPIView(views.APIView):
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


class FeedbackAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instance = Feedback.objects.all()
            return response.Response({'Feedback list': FeedbackSerializer(instance, many=True).data})

        try:
            instance = Feedback.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        return response.Response({'Detail': FeedbackSerializer(instance).data})

    def post(self, request):

        request.data['user'] = request.user.pk
        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Feedback created': serializer.data})

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        try:
            instance = Feedback.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        serializer = FeedbackSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Feedback update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        try:
            instance = Feedback.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.delete()

        return response.Response({'Feedback deleted': f'Запись {pk} удалена'})


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


class ChartAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            instance = Chart.objects.all()
            return response.Response({'Charts list': ChartSerializer(instance, many=True).data})

        try:
            instance = Chart.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        return response.Response({'Detail': ChartSerializer(instance).data})

    def post(self, request):

        request.data['user'] = request.user.pk
        serializer = ChartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Charts created': serializer.data})

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        try:
            instance = Chart.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        if request.data:
            instance.date_change = datetime.datetime.now()

        serializer = ChartSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Charts update': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if not pk:
            return response.Response({'Error': 'PK not defined'})

        try:
            instance = Chart.objects.get(pk=pk)
        except:
            return response.Response({'ORM error': 'Not data'})

        instance.delete()

        return response.Response({'Charts deleted': f'Запись {pk} удалена'})
