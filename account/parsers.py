import csv
from typing import List

from django.core.files.storage import default_storage

from account.logic.account_named_tuple import AccountNamedTuple


class CSVFileParser:
    __slots__ = ('file', 'path_file', 'values', 'list_accounts')
    resolved_format_file = 'csv'

    def __init__(self, file):
        self.file = self.validate_format_file(file)
        self.path_file = self.save_in_storage()
        self.list_accounts = self.parse_file()

    def validate_format_file(self, file):
        format_ = file.name.split('.')[-1]
        if format_ != self.resolved_format_file:
            raise TypeError(f'Недопустимый формат файла {format_}')
        else:
            return file

    def save_in_storage(self):
        file = default_storage.save(self.name, self.file)
        return file

    def parse_file(self) -> List[AccountNamedTuple]:
        list_accounts = []
        with open(self.path_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, organisation, number_of_account, sum_, date_, service = row.values()
                account = AccountNamedTuple(name=name,
                                            organisation=organisation,
                                            number_of_account=number_of_account,
                                            sum=sum_,
                                            date=date_,
                                            service=service)
                list_accounts.append(account)
        return list_accounts

    @property
    def name(self) -> str:
        return self.file.name


