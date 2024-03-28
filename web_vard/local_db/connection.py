from rest_framework import views, response

from sqlalchemy import create_engine


class ConnectDBAPIView(views.APIView):
    def post(self, request):

        try:
            db_user = request.data['User']
            db_pass = request.data['Password']
            db_driver = request.data['Driver']
            url = request.data['URL']
            db_host = request.data['Host']
            db_port = request.data['Port']
            data_base_type = request.data['Data Base Type']
            db_name = request.data['Data Base']
            description = request.data['Description']
        except KeyError:
            return response.Response('The form is not completed')

        my_sql_database = f'mysql+{db_driver}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        engine = create_engine(my_sql_database, echo=True)

        try:
            engine.connect()
        except:
            return response.Response({'Data error': 'One of the fields is filled in incorrectly'})

        return response.Response({'Success': 'Connected to db'})
