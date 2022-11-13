from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from convert_link.models import ShortLink
from .forms import *
from .utils import generate_short_link, link_check, get_owner
from django.contrib import messages
from datetime import datetime


def jump(request, short_link):
    link_obj = ShortLink.objects.filter(short_link=short_link).filter(deleted=False).first()
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
            short_link = generate_short_link(6)
            source_link = str(request.POST['source_link'])
            if link_check(source_link):
                messages.success(request, f'Вдало згенеровано нове коротке посилання: { short_link }')
                new_short_link = ShortLink(source_link=source_link, short_link=short_link, owner=owner)
                new_short_link.save()
                form = SourceLinkForm()
            else:
                messages.error(request, 'Посилання неактуальне. Перевірте правильність.')
        else:
            messages.error(request, 'Неправильний формат вихідного посилання. Введіть коректні дані та спробуйте знову.')
    ctx = {
        'form': form,
        'owner': owner
    }
    return render(request, 'index.html', ctx)


class LinkAPI(APIView):
    def get(self, request):
        lst = ShortLink.objects.filter(owner=get_owner(self.request)).filter(deleted=False).values()
        return Response({'short_links': list(lst)})

    def post(self, request):
        source_link = self.request.data['source_link']
        if link_check(source_link):
            short_link = generate_short_link(6)
            new_short_link = ShortLink.objects.create(
                source_link=source_link,
                short_link=short_link,
                owner=get_owner(self.request)
            )
            source_link = ''
            return Response({"message": model_to_dict(new_short_link)})
        else:
            return Response({"error": 'Не вдалося створити коротке посилання.'})
    permission_classes = (IsAuthenticatedOrReadOnly,)


# class ShortLinkList(generics.ListAPIView):
#     # queryset = ShortLink.objects.all()
#     def get_queryset(self):
#         owner = get_owner(self.request)
#         return ShortLink.objects.filter(owner=owner).filter(deleted=False)
#
#     serializer_class = ShortLinkSerializer
#     permission_classes = (IsAdminOrReadOnly,)

# class ShortLinkAPIList(generics.ListCreateAPIView):
#     # queryset = ShortLink.objects.all()
#     serializer_class = ShortLinkSerializer
#
#     def get_queryset(self):
#         if self.request.user.pk:
#             user = self.request.user.pk
#         else:
#             user = self.request.META.get("REMOTE_ADDR")
#         return ShortLink.objects.filter(owner=user).filter(deleted=False)
#     permission_classes = (IsAdminOrReadOnly,)
#
#
# class ShortLinkAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = ShortLink.objects.all()
#     serializer_class = ShortLinkSerializer
#     permission_classes = (IsOwnerOrReadOnly, )
#
#
# class ShortLinkAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = ShortLink.objects.all()
#     serializer_class = ShortLinkSerializer
#     permission_classes = (IsAdminOrReadOnly, )
