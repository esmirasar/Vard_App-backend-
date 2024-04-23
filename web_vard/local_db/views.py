from rest_framework import views, response

from sqlalchemy import create_engine, orm, text

from .models import Connection
from .serializers import ConnectionSerializer


class GetListConnectionAPIView(views.APIView):

    permission_classes = []

    def get(self, request):

        instance = Connection.objects.filter(user_id=request.user.pk, connection=True)

        return response.Response({'Data': ConnectionSerializer(instance, many=True).data})


class PostConnectionAPIView(views.APIView):

    permission_classes = []

    def post(self, request):

        request.data['user'] = request.user.pk
        print(request.data, )
        try:
            db_user = request.data['username']
            db_pass = request.data['password']
            db_driver = request.data['driver']
            url = request.data['url']
            db_host = request.data['host']
            db_port = request.data['port']
            data_base_type = request.data['data_base_type']
            db_name = request.data['name']
            description = request.data['description']
        except ValueError:
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


class ShowUserDataBaseAPIView(views.APIView):

    def get(self, request, *args, **kwargs):

        connect = Connection.objects.filter(user_id=request.user.pk, connection=True)

        return response.Response({'Your connections': ConnectionSerializer(connect, many=True).data})


class WorkDataBaseAPIView(views.APIView):
    def get(self, request, *args, **kwargs):

        try:
            connect = Connection.objects.get(pk=kwargs['pk'], user_id=request.user.pk, connection=True)
        except:
            return response.Response({'Error': 'Data not found'})

        url_connect = f'mysql+{connect.driver}://{connect.username}:{connect.password}@{connect.host}:{connect.port}/{connect.name}'
        engine = create_engine(url_connect)
        engine.connect()

        return response.Response({'Check': ConnectionSerializer(connect).data})

    def post(self, request, *args, **kwargs):

        try:
            connect = Connection.objects.get(pk=kwargs['pk'], user_id=request.user.pk, connection=True)
        except:
            return response.Response({'Error': 'Data not found'})

        url_connect = f'mysql+{connect.driver}://{connect.username}:{connect.password}@{connect.host}:{connect.port}/{connect.name}'
        engine = create_engine(url_connect)
        engine.connect()

        with orm.Session(autoflush=False, bind=engine) as db:
            try:
                result_1 = db.execute(text(f'{request.data["text"]}')).mappings().all()
            except:
                return response.Response({'Error': 'Try again'})

        return response.Response({'Data': result_1})
