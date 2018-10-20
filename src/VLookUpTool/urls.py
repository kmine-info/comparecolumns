from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'VLookUpTool'

from . import views

from .views import Vlookup
urlpatterns = [
            url(r'^(?i)vlookupform', Vlookup.as_view(), name='vlookupform'),
]

