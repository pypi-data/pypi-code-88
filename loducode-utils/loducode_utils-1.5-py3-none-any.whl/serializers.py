from rest_framework import serializers

from loducode_utils.models.city import City


class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'created_at', 'modified_at','created_by','modified_by')
        read_only_fields = ('created_at', 'modified_at','created_by','modified_by')

class CitySerializer(AuditSerializer):
    class Meta(AuditSerializer.Meta):
        model = City
        fields = AuditSerializer.Meta.fields + ('name', 'state')
