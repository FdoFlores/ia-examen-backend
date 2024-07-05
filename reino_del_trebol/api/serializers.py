from rest_framework import serializers
from .models import Mage

class MageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mage
        fields = '__all__'
        read_only_fields = ('custom_id', 'status')

class MagePatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mage
        fields = ['status']