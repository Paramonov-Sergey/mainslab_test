from rest_framework import serializers

from account.models.account import Account

INPUT_FORMATS_DATE = [
    '%d.%m.%Y',
    '%Y.%m.%d',

]


class AccountListCreateSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=INPUT_FORMATS_DATE)
    sum = serializers.CharField()
    number_of_account = serializers.CharField()

    class Meta:
        model = Account
        fields = '__all__'

    @staticmethod
    def validate_service(value):
        if any((not value,
                len(value) == 1 and value == "-")):
            raise serializers.ValidationError("Поле service не может быть пустым либо содержать единственный знак '-'")
        return value

    @staticmethod
    def validate_sum(value):
        try:
            sum_ = float(value)
        except ValueError:
            raise serializers.ValidationError("Вы должны передать число в поле sum")
        else:
            return sum_

    @staticmethod
    def validate_number_of_account(value):
        try:
            number_of_account = int(value)
        except ValueError:
            raise serializers.ValidationError("Вы должны передать целое число в поле number_of_account")
        return number_of_account


class AccountFileLoadSerializer(serializers.Serializer):
    file = serializers.FileField()
