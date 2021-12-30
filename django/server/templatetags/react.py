from server.settings import DEBUG
from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def react(js_file_name: str):
    r"""Connecting with the WebPackDev or Django Static
    setting from "REACT_DEV_URL", "REACT_HOST_URL"""
    if DEBUG == True:
        URL_HEAD = settings.REACT_DEV_URL
    else:
        URL_HEAD = settings.REACT_HOST_URL
    return f"{URL_HEAD}{js_file_name}"
