import os

"""
base.py 에도 os를 import 했기 때문에 파이참 에서 인식 하지 못하는 오류가 나서
모든 조건문에 settings.base 를 import 했음
"""

if os.environ.get("ENV_NAME") == "Production":
    from miniproject.settings.base import *
    from miniproject.settings.production import *

elif os.environ.get("ENV_NAME") == "Development":
    from miniproject.settings.base import *
    from miniproject.settings.development import *

else:
    from miniproject.settings.base import *
    from miniproject.settings.production import *
