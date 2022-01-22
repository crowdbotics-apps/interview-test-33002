from rest_framework import serializers

from app.models import Apps


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apps
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'type': {'required': True},
            'framework': {'required': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        app = Apps.objects.create(user=user, **validated_data)
        return app