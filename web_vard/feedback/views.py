from rest_framework import views, response

from web_vard.permissions import OnlyStaff

from .serializers import FeedbackSerializer
from .models import Feedback


class AllFeedbackAPIView(views.APIView):

    permission_classes = [OnlyStaff, ]

    def get(self, request, **kwargs):

        instance = Feedback.objects.all()

        return response.Response({'Data list': FeedbackSerializer(instance, many=True).data})


class GetPostFeedbackAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        if kwargs.get('my_feedback') != 'my_feedback':
            return response.Response({'Error': 'Data not defined'})

        instance = Feedback.objects.filter(user_id=request.user.pk)

        return response.Response({'My feedback': FeedbackSerializer(instance, many=True).data})

    def post(self, request, **kwargs):

        if kwargs.get('my_feedback') != 'my_feedback':
            return response.Response({'Error': 'Data not defined'})

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        request.data['user'] = request.user.pk

        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Feedback created': serializer.data})


class PutDeleteFeedbackAPIView(views.APIView):
    def get(self, request, **kwargs):

        my_feedback = kwargs.get('my_feedback')
        pk = kwargs.get('pk')
        instance = Feedback.objects.filter(user_id=request.user.pk).values('pk')

        if my_feedback != 'my_feedback' or {'pk': pk} not in instance:
            return response.Response({'Error': 'Data not defined'})

        instance = Feedback.objects.get(pk=pk)

        return response.Response({'Data': FeedbackSerializer(instance).data})

    def put(self, request, *args, **kwargs):

        my_feedback = kwargs.get('my_feedback')
        pk = kwargs.get('pk')
        instance = Feedback.objects.filter(user_id=request.user.pk).values('pk')

        if my_feedback != 'my_feedback' or {'pk': pk} not in instance:
            return response.Response({'Error': 'Data not defined'})

        if not request.data:
            return response.Response({'Error': 'Not data for change'})

        instance = Feedback.objects.get(pk=pk)

        serializer = FeedbackSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Feedback update': serializer.data})

    def delete(self, request, *args, **kwargs):

        my_feedback = kwargs.get('my_feedback')
        pk = kwargs.get('pk')
        instance = Feedback.objects.filter(user_id=request.user.pk).values('pk')

        if my_feedback != 'my_feedback' or {'pk': pk} not in instance:
            return response.Response({'Error': 'Data not defined'})

        instance = Feedback.objects.get(pk=pk)

        instance.delete()

        return response.Response({'Data delete': f'Data <{pk}> was deleted'})
