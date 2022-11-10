from django.contrib import admin
from django.urls import path
from convert_link.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/shortlinks', ShortLinkAPIList.as_view()),
    path('api/shortlink/<int:pk>', ShortLinkAPIUpdate.as_view()),
    path('api/delshortlink/<int:pk>', ShortLinkAPIDestroy.as_view()),
]
