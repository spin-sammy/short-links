from django.contrib import admin

from .models import ShortLink


class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('short_link', 'source_link', 'jumps', 'last_jump_at', 'active', 'owner')
    list_display_links = ('source_link',)
    search_fields = ('source_link', 'owner')


admin.site.register(ShortLink, ShortLinkAdmin)
