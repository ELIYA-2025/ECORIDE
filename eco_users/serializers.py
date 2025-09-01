from rest_framework import serializers
from django.contrib.auth.models import User
from .models import customer, Driver # Make sure 'customer' is correctly spelled here

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class customerSignupSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = customer # Changed from Rider to customer
        fields = ['user', 'phone', 'location']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        # ⚠️ This line is crucial. You were trying to create a Rider object.
        # It must be changed to create a customer object.
        customer_obj = customer.objects.create(user=user, **validated_data)
        return customer_obj

class DriverSignupSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Driver
        fields = ['user', 'phone', 'vehicle_number', 'vehicle_type', 'location']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        driver = Driver.objects.create(user=user, **validated_data)
        return driver