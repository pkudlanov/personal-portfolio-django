from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Project
from .forms import ContactForm


def home(request):
    form = ContactForm()

    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'form': form})


def send_email(request):
    send_form = ContactForm(request.POST)
    if send_form.is_valid():
        # name = form.cleaned_data['name']
        from_email = send_form.cleaned_data['from_email']
        subject = send_form.cleaned_data['subject']
        message = send_form.cleaned_data['message']
        try:
            send_mail(subject, message, from_email, ['me@kudlanov.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return JsonResponse({'success_message': 'Your voice is on its way to be heard by me!'})
    return JsonResponse({'error': 'Not able to validate form'})


def test(request):
    return render(request, 'portfolio/test.html')
