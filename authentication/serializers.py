from rest_framework import serializers
# from django.contrib.auth.models import User
from authentication.models import User



# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)
        # user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user