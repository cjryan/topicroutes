"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.views.generic import View
from django.core.urlresolvers import reverse

from .forms import ContactForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class ContactSuccessView(View):
    template_name = 'contact/success.html'
    def get(self, request, *args, **kargs):
        return render(
            request,
            self.template_name,
            {
                'title': 'Contact Success',
                'message': 'Thank you for your interest, we will be in touch.',
                'year': datetime.now().year,
            }
        )

class ContactFormView(View):
    form_class = ContactForm
    template_name = 'contact/contact.html'

    def get(self, request, *args, **kargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            #TODO send a registration email.
            return HttpResponseRedirect(reverse('contact_success'))
        return render(request, self.template_name, {'form': form})

