from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters
import requests


def generate_short_link(short_link_length: int = 6) -> str:
    short_link = ''.join(choice(ascii_lowercase + ascii_uppercase + digits + '-')
                         for i in range(short_link_length))
    return short_link


def link_check(link: str) -> bool:
    try:
        response = requests.get(link)
        return True
    except:
        return False
