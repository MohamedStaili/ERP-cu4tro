from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups", "password", "first_name", "last_name", "is_active"]
        extra_kwargs = {
            "password": {"write_only": True},
        }
    def create(self, validated_data):
        groups = validated_data.pop('groups', [])
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user.groups.set(groups)
        return user

    def update(self, instance, validated_data):
        groups = validated_data.pop('groups', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        if groups is not None:
            instance.groups.set(groups)
        return instance

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Group
        fields=["name"]

