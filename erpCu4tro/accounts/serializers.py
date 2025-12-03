from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True,
         slug_field="name",
         queryset=Group.objects.all(),
         required=False,
         write_only= True,
         )
    groups_display = serializers.StringRelatedField(
        source='groups',
        many=True,
        read_only=True
    )
    supervisor = serializers.PrimaryKeyRelatedField(
        source='profile.supervisor',   
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        write_only=True,
    )
    supervisor_display = serializers.StringRelatedField(
        source='profile.supervisor',
        read_only=True,
    )
    class Meta:
        model = User
        fields = [
            "id", "username", "email",
            "groups", "groups_display",
            "supervisor", "supervisor_display",
            "password", "first_name", "last_name", "is_active",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
    def create(self, validated_data):
        groups = validated_data.pop('groups', [])
        profile_data = validated_data.pop('profile', {})
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        if groups:
            user.groups.set(groups)
        supervisor = profile_data.get('supervisor')
        if supervisor is not None:
            user.profile.supervisor = supervisor
            user.profile.save()
        return user

    def update(self, instance, validated_data):
        groups = validated_data.pop('groups', None)
        profile_data = validated_data.pop('profile', {})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        if groups is not None:
            instance.groups.set(groups)
        if "supervisor" in profile_data:
            instance.profile.supervisor = profile_data["supervisor"]
            instance.profile.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Group
        fields=["name"]

