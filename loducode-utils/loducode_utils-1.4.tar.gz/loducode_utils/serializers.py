from rest_framework import serializers

from loducode_utils.models.city import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'state')
