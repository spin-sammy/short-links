from rest_framework import serializers
from .models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ('pk', 'source_link', 'short_link', 'jumps', 'updated_at', 'owner')
