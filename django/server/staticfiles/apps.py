# https://itinerant.tistory.com/144
# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#customizing-the-ignored-pattern-list
# Customizing the ignored pattern list
from django.contrib.staticfiles.apps import StaticFilesConfig


class StaticFilesConfig(StaticFilesConfig):
    # name = "collectstatic"
    ignore_patterns = [
        "node_modules",
        "src",
        ".env",
        ".babelrc",
        "*.json",
        "*.lock",
    ]