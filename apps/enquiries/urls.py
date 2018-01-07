from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'enquiries'

urlpatterns = [
    url(r'^email/$',views.send_email_view,name='email'),
]