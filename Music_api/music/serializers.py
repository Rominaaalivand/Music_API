from django.utils import timezone
from rest_framework import serializers
from .models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'genre', 'release_date']

    def validate_title(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Title must only contain letters")
        return value

    def validate_release_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Release date cannot be in the future")
        return value
