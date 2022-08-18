from rest_framework import serializers
from .models import GodModel, TYPE_CHOICES, TYPE1, TYPE2, TYPE3


class GodSerializer(serializers.ModelSerializer):
    class Meta:
        model = GodModel
        fields = ["my_type"]

    class Type1Serializer(serializers.ModelSerializer):
        my_type = serializers.ChoiceField(choices=TYPE_CHOICES)
        for_type1 = serializers.CharField()

        class Meta:
            model = GodModel
            fields = ["my_type", "for_type1"]

    class Type2Serializer(serializers.ModelSerializer):
        my_type = serializers.ChoiceField(choices=TYPE_CHOICES)
        for_type2 = serializers.CharField()

        class Meta:
            model = GodModel
            fields = ["my_type", "for_type2"]

    class Type3Serializer(serializers.ModelSerializer):
        my_type = serializers.ChoiceField(choices=TYPE_CHOICES)
        for_type3 = serializers.IntegerField()

        class Meta:
            model = GodModel
            fields = ["my_type", "for_type3"]

    def to_representation(self, god):
        custom_serializers = {
            TYPE1: self.Type1Serializer,
            TYPE2: self.Type2Serializer,
            TYPE3: self.Type3Serializer
        }
        if god.my_type in custom_serializers.keys():
            serializer = custom_serializers[god.my_type](god, context=self.context)
            return serializer.data
        else:
            return {}
