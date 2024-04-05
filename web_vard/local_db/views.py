from rest_framework import views, response

from sqlalchemy import create_engine, orm, text

from .models import Connection
from. serializers import ConnectionSerializer
from user.serializers import UserSerializer


class GetListConnectionAPIView(views.APIView):

    permission_classes = []

    def get(self, request):

        instance = Connection.objects.filter(user_id=request.user.pk, connection=True)

        return response.Response({'Data': ConnectionSerializer(instance, many=True).data})


class PostConnectionAPIView(views.APIView):

    permission_classes = []

    def post(self, request):

        request.data['user'] = request.user.pk

        try:
            db_user = request.data['username']
            db_pass = request.data['password']
            db_driver = request.data['driver']
            url = request.data['url']
            db_host = request.data['host']
            db_port = request.data['port']
            data_base_type = request.data['data_base_type']
            db_name = request.data['name']
            description = request.data['comment']
        except KeyError:
            return response.Response({'The form is not completed'})

        url_connect = f'mysql+{db_driver}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

        try:
            engine = create_engine(url_connect)
            engine.connect()
        except:
            return response.Response({'Data error': 'One of the fields is filled in incorrectly'})
        else:
            request.data['connection'] = True

        serializer = ConnectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response({'Data': serializer.data})
