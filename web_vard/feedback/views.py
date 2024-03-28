from rest_framework import views, response

from .serializers import FeedbackSerializer
from .models import Feedback


class GetPostFeedbackAPIView(views.APIView):
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


class PutDeleteFeedbackAPIView(views.APIView):
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

