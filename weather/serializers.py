from rest_framework import serializers

from weather.models import Place, WeatherReport


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    def validate(self, attrs):
        if not -180 <= attrs['longitude'] <= 180 or \
                not -90 <= attrs['latitude'] <= 90:
            raise serializers.ValidationError('Coordinates out of bounds')
        if not 0 <= attrs['rating'] <= 25:
            raise serializers.ValidationError('Rating must be between 0 and 25')
        return attrs


class WeatherReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherReport
        fields = '__all__'
