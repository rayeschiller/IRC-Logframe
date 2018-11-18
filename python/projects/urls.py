from django.conf.urls import url
from rest_framework import routers

from .views import *

app_name = "projects"

router = routers.SimpleRouter()
router.register(r'logframes', ProjectsViewSet)

urlpatterns = router.urls
