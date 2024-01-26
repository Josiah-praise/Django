from django.urls import path
from .views import *

app_name = "Pages"

urlpatterns = [path("", home_page_view, name="home_page")]
