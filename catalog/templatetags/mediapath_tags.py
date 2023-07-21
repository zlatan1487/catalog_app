from django import template

register = template.Library()


@register.simple_tag
def mediapath(img_path: str):
    """convert relative path to absolute path"""
    return f'/media/{img_path}'