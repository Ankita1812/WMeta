from rest_framework import serializers
from .models import Images,Member


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Images
        fields= [
            'title',
            'description',
            'image'
        ]

class ItemSerializer1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Member
        fields= [
            'name',
            'post',
            'image',
            'phn_number',
            'email',
            'info',
            'address'

                    ]
