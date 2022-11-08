from rest_framework import generics, viewsets
from convert_link.models import ShortLink, User
from convert_link.serializers import ShortLinkSerializer


class ShortLinkAPIList(generics.ListCreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer


class ShortLinkAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer


class ShortLinkAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer
