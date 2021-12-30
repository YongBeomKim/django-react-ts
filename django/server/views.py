import json
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"