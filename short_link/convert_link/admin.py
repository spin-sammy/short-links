from django.contrib import admin

from .models import ShortLink

# admin.site.register(User)


class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('short_link', 'jumps', 'last_jump_at', 'owner')
    list_display_links = ('short_link',)
    search_fields = ('short_link', 'owner')


admin.site.register(ShortLink, ShortLinkAdmin)
