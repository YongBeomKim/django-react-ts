# https://hikoding.tistory.com/49
# https://docs.djangoproject.com/en/4.0/topics/logging/#loggers
# DEBUG (디버깅) INFO(정보) WARNING (마이너) 
# ERROR (오류) CRITICAL (문제발생)
LOG_FOLDER = "../logs/"

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'encoding': 'utf-8',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR.joinpath(LOG_FOLDER + 'django.log'),
            'maxBytes': 1024*1024*1,  # 5 MB
            'backupCount': 5,         # 최대 파일갯수
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'my': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}