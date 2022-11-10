from rest_framework import serializers
from .models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ShortLink
        fields = ('pk', 'source_link', 'short_link', 'jumps', 'updated_at', 'owner')
