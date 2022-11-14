from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
import requests
from .models import ShortLink


def generate_short_link(short_link_length: int = 6) -> str:
    short_link = ''.join(choice(ascii_lowercase + ascii_uppercase + digits + '-')
                         for i in range(short_link_length))
    return short_link


def link_check(link: str) -> bool:
    try:
        check = requests.head(link)
        return True
    except:
        return False


def get_owner(request) -> str:
    if str(request.user) != 'AnonymousUser':
        user_title = str(request.user.pk)
    else:
        user_title = str(request.META.get("REMOTE_ADDR"))
    return user_title


def check_deleted_link(source_link: str) -> bool:
    deleted_links = ShortLink.objects.filter(active=False).values()
    for item in deleted_links:
        if item['source_link'] == source_link:
            return True
    return False
