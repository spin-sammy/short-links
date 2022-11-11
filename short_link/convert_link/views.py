from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import render, redirect
from convert_link.models import ShortLink, User
from convert_link.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from convert_link.serializers import ShortLinkSerializer
from .forms import *
from .utils import generate_short_link


def index(request):
    form = SourceLinkForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if str(request.user) != 'AnonymousUser':
                print(request.user)
                print('-= ALL OK =-')
                print(generate_short_link(10))
            else:
                print(f'Not authenticated user: {request.META.get("REMOTE_ADDR")}')

    ctx = {
        'form': form
    }
    return render(request, 'index.html', ctx)


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
