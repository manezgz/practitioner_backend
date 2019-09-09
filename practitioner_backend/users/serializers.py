from rest_framework_mongoengine import serializers

from .models import Users

class UsersSerializer(serializers.DocumentSerializer):
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.mobile_phone = validated_data.get('mobile_phone', instance.mobile_phone)
        instance.save()
        return instance

    def validate(self, data):
        print(data)
        return data

    class Meta:
        model = Users
        fields = ('email','first_name','last_name','mobile_phone','isActive')
