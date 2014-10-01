import os

from django.conf import settings


def items():
    items = [
        dict(
            location='/matlab/streaming-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'matlab',
                'streaming-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/matlab/user-guide/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'matlab',
                'user-guide',
                'body.html'),
            priority=0.5
        )
    ]
    return items
