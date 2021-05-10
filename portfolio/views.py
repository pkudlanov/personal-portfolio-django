from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Project
from .forms import ContactForm


def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['me@kudlanov.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, ('Email sent successfully.'))
            return redirect('home')

    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'form': form})


def test(request):
    return render(request, 'portfolio/test.html')
