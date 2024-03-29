import datetime

from rest_framework import views, response

from web_vard.permissions import OnlyStaff, PerCustom

from .serializers import ChartSerializer
from .models import Chart


class ListChartAPIView(views.APIView):

    permission_classes = [OnlyStaff, ]

    def get(self, request):

        instance = Chart.objects.all()

        return response.Response({'List data': ChartSerializer(instance, many=True).data})


class GetPostChartAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    def get(self, request, *args, **kwargs):
        if kwargs.get('my_chart') != 'my_chart':
            return response.Response({'Error': 'Data not defined'})

        instance = Chart.objects.filter(user_id=request.user.pk)

        return response.Response({'Detail': ChartSerializer(instance).data})

    def post(self, request, **kwargs):

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        if kwargs.get('my_chart') != 'my_chart':
            return response.Response({'Error': 'Data not defined'})

        request.data['user'] = request.user.pk

        serializer = ChartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Charts created': serializer.data})


class PutDeleteChartAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    def get(self, request, **kwargs):

        my_chart = kwargs.get('my_chart')
        pk = kwargs.get('pk')
        instance = Chart.objects.filter(user_id=request.user.pk).values('pk')

        if my_chart != 'my_chart' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Chart.objects.get(pk=pk)

        return response.Response({'Data': ChartSerializer(instance).data})

    def put(self, request, *args, **kwargs):

        if not request.data:
            return response.Response({'Error': 'Enter data'})

        my_chart = kwargs.get('my_chart')
        pk = kwargs.get('pk')
        instance = Chart.objects.filter(user_id=request.user.pk).values('pk')

        if my_chart != 'my_chart' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Chart.objects.get(pk=pk)

        instance.date_change = datetime.datetime.now()

        serializer = ChartSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Charts update': serializer.data})

    def delete(self, request, *args, **kwargs):

        my_chart = kwargs.get('my_chart')
        pk = kwargs.get('pk')
        instance = Chart.objects.filter(user_id=request.user.pk).values('pk')

        if my_chart != 'my_chart' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Chart.objects.get(pk=pk)

        instance.delete()

        return response.Response({'Charts deleted': f'Запись {pk} удалена'})
