from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['email'],
    #          validated_data['password'])
    #     return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

class MyRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }