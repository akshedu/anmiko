from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
             validated_data['password'],
             first_name=validated_data['first_name'],
             last_name=validated_data['last_name'])

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')