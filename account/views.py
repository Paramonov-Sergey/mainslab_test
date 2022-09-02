import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from account.logic.load_accounts import AccountLoaderCSVFile
from account.mixins import ListCreateModelViewSet
from account.models.account import Account
from account.serializers import AccountListCreateSerializer, AccountFileLoadSerializer


class AccountViewSet(ListCreateModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class_by_action = {'list': AccountListCreateSerializer,
                                  'create': AccountListCreateSerializer,
                                  'load_accounts': AccountFileLoadSerializer}
    queryset = Account.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'organisation']

    def get_serializer_class(self, action=None):
        action = self.action if action is None else action
        serializer_class = self.serializer_class_by_action.get(action)
        return serializer_class

    def load_accounts(self, request, *args, **kwargs):
        """Загрузка CSV файла с счетами"""
        try:
            serializer = self.get_serializer_class(action='create')
            loader = AccountLoaderCSVFile(request)
            loader.create_in_db(serializer)
        except Exception as e:
            message_error = {
                "message": e.args[0]
            }
            data = json.dumps(message_error)
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            serializer = self.get_serializer_class(action='list')
            data = loader.get_response_data(serializer)
            return Response(data, status=status.HTTP_201_CREATED)
