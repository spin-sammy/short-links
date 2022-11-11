from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import render, redirect
from convert_link.models import ShortLink, User
from convert_link.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from convert_link.serializers import ShortLinkSerializer
from .forms import *
from .utils import generate_short_link, link_check
from django.contrib import messages


def index(request):
    form = SourceLinkForm(request.POST)
    if str(request.user) != 'AnonymousUser':
        user_title = str(request.user)
    else:
        user_title = str(request.META.get("REMOTE_ADDR"))
    if request.method == 'POST':
        if form.is_valid():
            short_link = generate_short_link(6)
            print(request.user)
            print('-= ALL OK =-')
            print(short_link)
            print(request.POST['source_link'])
            source_link = str(request.POST['source_link'])
            if link_check(source_link):
                messages.success(request, f'Успешно сгенерирована новая короткая ссылка: { short_link }')
                form = SourceLinkForm()
            else:
                messages.error(request, 'К сожалению ссылка никуда не ведет. Проверьте правильность.')
        else:
            messages.error(request, 'Неправильный формат исходной ссылки. Введите корректные данные и попробуйте снова.')
    ctx = {
        'form': form,
        'user_title': user_title
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
