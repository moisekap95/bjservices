from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView, FormView)
from . import models

from django.db.models import Q
from django.shortcuts import redirect, render

# Create your views here.

#CRUD Views

class TeamMemberListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    context_object_name = 'teammembers'
    model = models.TeamMember

class TeamMemberDetailView(DetailView):
    context_object_name = 'teammember_details'
    model = models.TeamMember
    template_name = 'teammembers/teammember_details.html'

class TeamMemberSearchView(ListView):
    template_name = 'teammembers/search_result.html'
    model = models.TeamMember
    context_object_name = 'teammembers'
    fieldsData = {}

    def get_queryset(self):
        #add fieldData to context dictionary
        self.fieldsData['name'] = self.request.GET['name']
        self.fieldsData['city'] = self.request.GET['city']
        self.fieldsData['state'] = self.request.GET['state']
        self.fieldsData['country'] = self.request.GET['country']

        name = self.request.GET['name']
        city = self.request.GET['city']
        state = self.request.GET['state']
        country = self.request.GET['country']

        if not self.model.objects.filter(city__icontains=city):
            city = ''
        if not self.model.objects.filter(state__icontains=state):
            state = ''
        if not self.model.objects.filter(country__icontains=country):
            country = ''

        return self.model.objects.filter(name__icontains=name, city__icontains=city, state__icontains=state, country__icontains=country)

    #def get_context_data(self,**kwargs):
        #context  = super().get_context_data(**kwargs)
        #congregation_search_form = forms.CongregationSearchForm()
        #context['congregation_search_form'] = congregation_search_form
        #context['fieldsData'] = self.fieldsData
        #return context

