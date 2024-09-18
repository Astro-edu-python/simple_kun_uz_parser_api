from rest_framework import serializers

from apps.api.v1.main.models import KunUzNews


class KunUzNewsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = KunUzNews
        fields = '__all__'
