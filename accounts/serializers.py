from accounts.models import Users
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        return token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users 
        fields = ['id', 'name', 'email', 'role', 'country', 'nationality', 'mobile']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True
    )

    class Meta:
        model = Users
        fields = ('username', 'name', 'password', 'confirm_password',
            'email', 'role', 'mobile', 'country', 'nationality')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            role=validated_data['role'],
            mobile=validated_data['mobile'],
            country=validated_data['country'],
            nationality=validated_data['nationality']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
