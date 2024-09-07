from rest_framework import serializers
from .models import UserProfile, Language, Country, Subscription


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    subscription_model = SubscriptionSerializer()
    country = CountrySerializer()
    language = LanguageSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        subscription_data = validated_data.pop('subscription_model', None)
        country_data = validated_data.pop('country', None)
        language_data = validated_data.pop('language', None)

        subscription = None
        if subscription_data:
            subscription, created = Subscription.objects.get_or_create(
                **subscription_data)

        country = None
        if country_data:
            country, created = Country.objects.get_or_create(**country_data)

        language = None
        if language_data:
            language, created = Language.objects.get_or_create(**language_data)

        user_profile = UserProfile.objects.create(
            subscription_model=subscription,
            country=country,
            language=language,
            **validated_data
        )
        return user_profile

    def update(self, instance, validated_data):
        subscription_data = validated_data.pop('subscription_model', None)
        country_data = validated_data.pop('country', None)
        language_data = validated_data.pop('language', None)

        if subscription_data:
            subscription, created = Subscription.objects.get_or_create(
                **subscription_data)
            instance.subscription_model = subscription

        if country_data:
            country, created = Country.objects.get_or_create(**country_data)
            instance.country = country

        if language_data:
            language, created = Language.objects.get_or_create(**language_data)
            instance.language = language

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
