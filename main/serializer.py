from rest_framework import serializers
from .models import NumberGenerateTask


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = NumberGenerateTask
        fields = ("id", "time", "status", "result")