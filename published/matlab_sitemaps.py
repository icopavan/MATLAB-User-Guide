from django.conf import settings
import os

def items():
    items = [
        dict(
            location='/matlab/line-and-scatter-plots-tutorial/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','matlab','line-and-scatter-plots-tutorial','body.html'),
            priority=0.5
        ),
        dict(
            location='/matlab/introduction/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','matlab','introduction','body.html'),
            priority=0.5
        ),
        dict(
            location='/matlab/user-guide/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','matlab','user-guide','body.html'),
            priority=0.5
        ),
        dict(
            location='/matlab/overview/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','matlab','overview','body.html'),
            priority=0.5
        )
    ]
    return items
