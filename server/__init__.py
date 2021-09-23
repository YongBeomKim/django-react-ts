# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

# the app is loaded when Django starts so that 
# the @shared_task decorator (mentioned later) will use it
from .celery import app as celery_app

__all__ = ('celery_app',)