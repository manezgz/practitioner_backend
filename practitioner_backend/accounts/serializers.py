from rest_framework_mongoengine import serializers

from .models import Accounts


class AccountSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'
