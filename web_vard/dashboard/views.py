import datetime

from rest_framework import views, response

from .models import Dashboard
from .serializers import DashboardSerializer


class GetPostDashBoardAPIView(views.APIView):
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


class DeletePutDashboardAPIView(views.APIView):
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
