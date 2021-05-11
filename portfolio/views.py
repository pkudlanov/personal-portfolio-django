from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

import json

# Including for debugging
# from pprint import pprint

from .models import Project
from .forms import ContactForm


def home(request):
    form = ContactForm()

    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'form': form})


def send_email(request):
    send_form = ContactForm(request.POST)
    data_valid = False
    if send_form.is_valid():
        data_valid = True
        # name = form.cleaned_data['name']
        from_email = send_form.cleaned_data['from_email']
        subject = send_form.cleaned_data['subject']
        message = send_form.cleaned_data['message']
        try:
            send_mail(subject, message, from_email, ['me@kudlanov.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return JsonResponse({
            'success_message': 'Your voice is on its way to be heard by me!',
            'data_valid': data_valid
        })
    return JsonResponse({
        'success_message': 'Not able to validate form',
        'form_errors': json.dumps(send_form.errors),
        'data_valid': data_valid
    })


def test(request):
    return render(request, 'portfolio/test.html')
