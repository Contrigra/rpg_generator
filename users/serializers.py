from rest_framework import serializers
from django.contrib.auth import get_user_model


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model()(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
