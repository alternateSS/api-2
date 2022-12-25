from rest_framework import serializers

from .models import *


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"


class labelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    office_address = serializers.DateTimeField()

    def create(self, validated_data):
        message = Label.objects.create(
            name=validated_data['name'],
            office_address=validated_data['office_address']
        )
        return message

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.office_address = validated_data['office_address']
        return instance