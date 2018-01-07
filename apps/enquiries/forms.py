from django import forms
from apps.enquiries.models import Enquiry
from apps.categories.models import Category

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Please Enter your Name *'}), required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Please Enter your Email *'}), required=True)
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'placeholder': 'Please Enter your Subject *'}), required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Please Enter your message *'}), required=True)
    category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all(), empty_label="Enquiry Category", required=False)

    class Meta():
        model = Enquiry
        exclude = ['date']
        fields = '__all__'