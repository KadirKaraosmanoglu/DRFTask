from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from api.models import Projects, Users


class ProjectCreateSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(read_only=True)

    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'start_date', 'deadline','created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'description', 'start_date', 'deadline']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Users
        fields = ['username', 'password', 'password2', 'isProjectManager']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Parolalar eşleşmedi"})

        return attrs

    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
            isProjectManager=validated_data['isProjectManager'])
        user.set_password(validated_data['password'])
        user.save()
        return user
