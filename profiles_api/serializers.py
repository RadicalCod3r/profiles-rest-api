from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class ProfileSerializer(serializers.ModelSerializer):
    """Creates a serializer for user profile model"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes Profile Feed Items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }

    # def create(self, validated_data):
    #     feed = models.ProfileFeedItem.objects.create(
    #         status_text = validated_data['status_text']
    #     )

    #     return feed