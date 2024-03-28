import datetime

from rest_framework import views, response

from .serializers import ChartSerializer
from .models import Chart


class GetPostChartAPIView(views.APIView):
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


class PutDeleteChartAPIView(views.APIView):
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
