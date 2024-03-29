import datetime

from rest_framework import views, response

from web_vard.permissions import OnlyStaff, PerCustom

from .models import Dashboard
from .serializers import DashboardSerializer


class ListDashboardAPIView(views.APIView):

    permission_classes = [OnlyStaff, ]

    def get(self, request):

        instance = Dashboard.objects.all()

        return response.Response({'List data': DashboardSerializer(instance, many=True).data})


class GetPostDashBoardAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    def get(self, request, *args, **kwargs):

        if kwargs.get('my_dashboard') != 'my_dashboard':
            return response.Response({'Error': 'Data not defined'})

        instance = Dashboard.objects.filter(user_id=request.user.pk)

        return response.Response({'Detail': DashboardSerializer(instance, many=True).data})

    def post(self, request, **kwargs):

        if kwargs.get('my_dashboard') != 'my_dashboard':
            return response.Response({'Error': 'Data not defined'})

        request.data['user'] = request.user.pk

        serializer = DashboardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Dashboard created': serializer.data})


class DeletePutDashboardAPIView(views.APIView):

    permission_classes = [PerCustom, ]

    def get(self, request, **kwargs):

        my_dashboard = kwargs.get('my_dashboard')
        pk = kwargs.get('pk')
        instance = Dashboard.objects.filter(user_id=request.user.pk).values('pk')

        if my_dashboard != 'my_dashboard' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Dashboard.objects.get(pk=pk)

        return response.Response({'Data': DashboardSerializer(instance).data})

    def put(self, request, *args, **kwargs):

        my_dashboard = kwargs.get('my_dashboard')
        pk = kwargs.get('pk')
        instance = Dashboard.objects.filter(user_id=request.user.pk).values('pk')

        if my_dashboard != 'my_dashboard' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Dashboard.objects.get(pk=pk)

        instance.date_change = datetime.datetime.now()

        serializer = DashboardSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data update': serializer.data})

    def delete(self, request, *args, **kwargs):

        my_dashboard = kwargs.get('my_dashboard')
        pk = kwargs.get('pk')
        instance = Dashboard.objects.filter(user_id=request.user.pk).values('pk')

        if my_dashboard != 'my_dashboard' or {'pk': pk} not in instance:
            return response.Response({'Error': 'data not defined'})

        instance = Dashboard.objects.get(pk=pk)

        instance.delete()

        return response.Response({'Data delete': f'Data <{pk}> was deleted'})
