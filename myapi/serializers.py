from rest_framework import serializers
from myapi.models import Hero

class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Hero
        fields = ('name', 'alias')