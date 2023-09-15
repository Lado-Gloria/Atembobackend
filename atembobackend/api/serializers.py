from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email',"first_name","last_name")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user




# from rest_framework import serializers
# from .models import CustomUser
# class CustomUserSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True, required=True)
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password',
#                   'confirm_password']
#         extra_kwargs = {'password': {'write_only': True}, 'confirm_password':
#             {'write_only': True}}
#     def create(self, validated_data):
#         confirm_password = validated_data.pop('confirm_password')
#         if validated_data['password'] != confirm_password:
#             raise serializers.ValidationError("Passwords do not match.")
#         user = CustomUser(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user