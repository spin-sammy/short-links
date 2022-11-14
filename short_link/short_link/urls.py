from django.contrib import admin
from django.urls import path, include
from convert_link.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/link', NewLinkAPI.as_view()),
    path('api/link/<str:short_link>', LinkAPI.as_view()),
    path('redirect/<str:short_link>', jump),
]
