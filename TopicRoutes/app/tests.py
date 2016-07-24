"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from app.forms import ContactForm

from django.core.urlresolvers import reverse

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact')

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)

class ContactFormTest(TestCase):
    """Tests for the application forms."""
    
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ContactFormTest, cls).setUpClass()
            django.setup()

    def test_contact(self):
        """Tests the contact form"""
        form_data = {'name': 'Jeremy',
                     'email_address': 'a@a.com',
                     'how_would_you_use': 'I would do awesome stuff.'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_missing_name_field(self):
        """Tests the contact missing a name"""
        form_data = {'email_address': 'a@a.com',
                     'how_would_you_use': 'I would do awesome stuff.'}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_contact_missing_use_field(self):
        """Tests the contact form missing the use field"""
        form_data = {'name': 'Jeremy',
                     'email_address': 'a@a.com',
                     }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_contact_missing_email_field(self):
        """Tests the contact form missing the use field"""
        form_data = {'name': 'Jeremy',
                     'how_would_you_use': 'I would do lame stuff',
                     }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        
    def test_contact_malformed_email(self):
        """Tests the contact form with a malformed email address"""
        form_data = {'name': 'Jeremy',
                     'email_address': 'a@a@l.com',
                     'how_would_you_use': 'I would do awesome stuff.'}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

class ContactFormViewTest(TestCase):

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ContactFormViewTest, cls).setUpClass()
            django.setup()

    def test_contact_form_view(self):
        form_data = {'name': 'Jeremy',
                     'email_address': 'a@a.com',
                     'how_would_you_use': 'I would do awesome stuff.'}
        response = self.client.post(reverse('contact'), form_data)
        self.assertRedirects(response, reverse('contact_success')) 

    def test_contact_form_view_invalid_data(self):
        form_data = {'name': 'Jeremy',
                     'email_address': 'a@a@l.com',
                     'how_would_you_use': 'I would do awesome stuff.'}
        response = self.client.post(reverse('contact'), form_data)
        self.assertContains(response, 'Enter a valid email address.') # assertFormError would probably be more robust.

