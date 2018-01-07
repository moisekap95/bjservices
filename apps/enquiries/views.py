from apps.texts.models import Text
from apps.categories.models import Category
from apps.enquiries.models import Enquiry
from apps.core.models import Company

#Email packages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def send_email_view(request):
    enquiries = Enquiry.objects.all()
    categories = Category.objects.all()
    companies = Company.objects.filter(name__icontains='BJ Services')
    texts = Text.objects.all()
    #Email 
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    if request.method == 'POST':   
        try:
            send_mail(subject, message  + '\n ' + name + '\n ' + phone, email, ['moisekapanda@gmail.com'])
            return render(request, 'enquiries/contact.html', {'name':name, 
                                                             'enquiries':enquiries, 
                                                             'categories':categories, 
                                                             'companies':companies, 
                                                             'texts':texts},)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    
    return render(request, 'enquiries/contact.html', {'name':name, 
                                                      'enquiries':enquiries, 
                                                      'categories':categories, 
                                                      'companies':companies, 
                                                      'texts':texts},)