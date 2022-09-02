from functools import cached_property
from typing import List

from account.logic.account_named_tuple import AccountNamedTuple
from account.models.account import Account
from account.parsers import CSVFileParser
from account.utils.exceptions.content_type import ContentTypeException


class AccountLoaderCSVFile:
    saved_models: list
    parser = CSVFileParser
    account_class = Account
    resolved_media_types = ('text/csv', 'multipart/form-data')
    encoding = 'utf-8'

    def __init__(self, request):
        self.request = request
        self.content_type = self.get_content_type()
        self.accounts = self.load_accounts()

    def create_in_db(self, serializer_class):
        """Создание аккаунтов в базе данных"""
        models = []
        for account in self.accounts:
            serializer = serializer_class(data=account._asdict())
            if serializer.is_valid(raise_exception=True):
                models.append(serializer)
        self.saved_models = [model.save() for model in models]

    def get_content_type(self):
        """Получение MIME типа"""
        content_type = self.request.content_type.split(';')[0].strip()
        return content_type

    def validate_content_type(self, content_type):
        """Проверка MIME типа передаваемого контента"""
        if content_type not in self.resolved_media_types:
            raise ContentTypeException("Error")

    @cached_property
    def file(self):
        """Получение файла"""
        file = self.request.data.get('file')
        return file

    def load_accounts(self) -> List[AccountNamedTuple]:
        """Загрузка и парсинг аккаунтов"""
        file = self.file
        accounts = self.parser(file).list_accounts
        return accounts

    def get_response_data(self, serializer_class):
        data = serializer_class(self.saved_models, many=True).data
        return data
