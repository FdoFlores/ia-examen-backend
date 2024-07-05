from rest_framework import serializers
from .models import Mage, Grimoire

class MageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mage
        fields = '__all__'
        read_only_fields = ('id', 'status', 'grimoire')

class MagePatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mage
        fields = ['status']

class GrimoireSerializer(serializers.ModelSerializer):
    grimoire_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Mage
        fields = ['id', 'name', 'last_name', 'grimoire_name']

    def get_grimoire_name(self, obj):
        return obj.grimoire.grimoire_name