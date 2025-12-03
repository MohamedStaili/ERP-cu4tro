from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Client

User = get_user_model()

class ClientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = [
            "id",
            "username",   
            "password",   
            "first_name",
            "last_name",
            "email",
            "phone",
        ]

    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            username=username,
            email=validated_data.get("email"),
            password=password,
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )

        try:
            client_group = Group.objects.get(name="client")
            user.groups.add(client_group)
        except Group.DoesNotExist:
            pass

        client = Client.objects.create(
            user=user,
            **validated_data,
        )

        return client
