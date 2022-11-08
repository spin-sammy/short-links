from django.contrib import admin
from django.urls import path
from convert_link.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shortlinks', ShortLinkAPIList.as_view()),
    path('api/shortlinks/<int:pk>', ShortLinkAPIUpdate.as_view()),
    path('api/shortlinks/del/<int:pk>', ShortLinkAPIDestroy.as_view()),
]
