from apps.enquiries import forms

from django.views.generic import ListView
from apps.services.models import Service
from apps.texts.models import Text
from apps.works.models import Work
from apps.skills.models import Skill
from apps.categories.models import Category
from apps.reviews.models import Review
from apps.enquiries.models import Enquiry
from apps.core.models import Company
from apps.teammembers.models import TeamMember


class IndexView(ListView):
    context_object_name = 'texts'
    #model = Work
    template_name = 'core/index.html'
    queryset = Text.objects.all()

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['services'] = Service.objects.all()[:3]
        context['works'] = Work.objects.order_by('id').reverse()[:4]
        context['skills'] = Skill.objects.all()
        context['categories'] = Category.objects.all()
        context['enquiries'] = Enquiry.objects.all()
        context['companies'] = Company.objects.filter(name__icontains='BJ Services')
        context['teammembers'] = TeamMember.objects.all()
        context['contact_form'] = forms.ContactForm
        return context