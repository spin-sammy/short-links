from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import render, redirect
from convert_link.models import ShortLink, User
from convert_link.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from convert_link.serializers import ShortLinkSerializer


def index(request):
    return render(request, 'index.html')


class ShortLinkAPIList(generics.ListCreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ShortLinkAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ShortLinkAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer
    permission_classes = (IsAdminOrReadOnly, )
