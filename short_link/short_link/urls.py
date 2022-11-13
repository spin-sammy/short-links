from django.contrib import admin
from django.urls import path, include
from convert_link.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/links', LinkAPI.as_view()),
    path('redirect/<str:short_link>', jump)
    # path('api/shortlink/<int:pk>', ShortLinkAPIUpdate.as_view()),
    # path('api/shortlink/del/<int:pk>', ShortLinkAPIDestroy.as_view()),
]
