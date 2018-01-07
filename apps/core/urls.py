from django.conf.urls import url,include
from . import views

# SET THE NAMESPACE!
app_name = 'core'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]