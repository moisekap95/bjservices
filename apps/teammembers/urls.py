from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'teammembers'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^list/$',views.TeamMemberListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.TeamMemberDetailView.as_view(),name='detail'),
    url(r'^search/$',views.TeamMemberSearchView.as_view(),name='search'),
]