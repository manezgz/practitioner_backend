from rest_framework_mongoengine import serializers

from .models import Transactions


class TransactionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
