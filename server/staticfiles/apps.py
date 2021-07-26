from django.contrib.staticfiles.apps import StaticFilesConfig


# Customizing the ignored pattern list¶
# https://itinerant.tistory.com/144
# https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#customizing-the-ignored-pattern-list
class StaticFilesConfig(StaticFilesConfig):
    # name = "collectstatic"
    ignore_patterns = [
        "node_modules",
        "css",
        "src",
        ".env",
        ".babelrc",
        "*.json",
        "*.lock",
    ]
