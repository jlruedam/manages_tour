from rest_framework import serializers
from sales.models import Client
from cities_light.models import Country, City

class ClientSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
