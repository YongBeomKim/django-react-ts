import json
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


# Todo React Testing Data
json_file_path = "static/src/data.json"
with open(json_file_path, "r") as json_data:
    content = json.loads(json_data.read())


def json_api(request):
    context = content["days"]
    print(context)
    return JsonResponse(context, json_dumps_params={"ensure_ascii": False}, safe=False)


def json_api_day(request, pk):
    context = [items for items in content["words"] if items["day"] == pk]
    return JsonResponse(context, json_dumps_params={"ensure_ascii": False}, safe=False)
