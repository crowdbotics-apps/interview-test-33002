from rest_framework import serializers

from app.models import Apps, Plan, Subscription


class AppSerializer(serializers.ModelSerializer):
    subscription = serializers.IntegerField(
        source="subscription.id",
        read_only=True
    )
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


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'active': {'required': True}
        }

    def create(self, validated_date):
        user = self.context['request'].user
        subscription = Subscription.objects.create(
            user=user,
            **validated_date
        )
        return subscription
