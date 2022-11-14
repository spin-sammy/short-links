from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from convert_link.models import ShortLink
from .forms import *
from .utils import generate_short_link, link_check, get_owner, check_deleted_link
from django.contrib import messages
from datetime import datetime


def jump(request, short_link):
    link_obj = ShortLink.objects.filter(short_link=short_link).filter(active=True).first()
    ext_link = link_obj.source_link
    link_obj.last_jump_at = datetime.now()
    link_obj.jumps += 1
    link_obj.save()
    return redirect(ext_link)


def index(request):
    form = SourceLinkForm(request.POST)
    owner = get_owner(request)
    if request.method == 'POST':
        if form.is_valid():
            short_link = generate_short_link()
            source_link = str(request.POST['source_link'])
            if link_check(source_link) and not check_deleted_link(source_link):
                messages.success(request, f'Вдало згенеровано нове коротке посилання: {short_link}')
                new_short_link = ShortLink(source_link=source_link, short_link=short_link, owner=owner)
                new_short_link.save()
                form = SourceLinkForm()
            else:
                messages.error(request, 'Посилання неактуальне. Перевірте правильність.')
        else:
            messages.error(request, 'Невірний формат вихідного посилання. Введіть коректні дані та спробуйте знову.')
    ctx = {
        'form': form,
        'owner': owner
    }
    return render(request, 'index.html', ctx)


class NewLinkAPI(APIView):
    def post(self, request):
        source_link = self.request.data['source_link']
        if link_check(source_link) and not check_deleted_link(source_link):
            short_link = generate_short_link(6)
            ShortLink.objects.create(source_link=source_link, short_link=short_link, owner=get_owner(self.request))
            source_link = ''
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    permission_classes = (AllowAny,)


class LinkAPI(APIView):
    def get(self, request, short_link):
        owner = get_owner(self.request)
        link_object = ShortLink.objects.filter(short_link=short_link).filter(active=True).filter(owner=owner).first()
        if link_object:
            jumps = link_object.jumps
            return Response({'jumps': jumps})
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, short_link):
        link_obj = ShortLink.objects.filter(short_link=short_link).filter(active=True).first()
        owner = link_obj.owner
        if owner == get_owner(self.request) and link_obj.active:
            link_obj.active = False
            link_obj.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    permission_classes = (AllowAny,)
