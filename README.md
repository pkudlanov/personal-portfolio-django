# personal-portfolio-django
Personal portfolio site based off of python/django. Built it after taking a few udemy courses. It was quite the experience. Got to get pretty comfortable with django/standardized class based views and more custom function based views. Played with django forms, error handling, custom form styling. Worked a lot with bootstrap styling. I think I can pretty comfortably say I got quite fimiliar with bootstrap. Scoured pretty much every single bootstrap docs page. Also in this personal portfolio project I had the chance to mess with deployment. I deployed the project on digitalocean. The learning curve wasn't very flat to say the least. Had really big issues with getting my static files to load. Kept getting that my static files/css were **mime** type, whatever that is. Then I just could not figure out how to load environment variables securely. Anyway, it was quite the project.

## Resources used for deployment
- [Digitalocean Django Deployment How-to](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)
  - Used this article the heaviest. For basic setup of the whole project.
  - Also in the end very heavy for troubleshooting gunicorn server. Reloading gunicorn stuff, restarting gunicorn server, restarting nginx.
  - It was also helpful after nuking PostgreSQL Database to set it backup.
- [YouTube Video Following Above Article](https://www.youtube.com/watch?v=BrVHwQ-SJUA)
  - Needed the video to correctly install the existing project dependencies. Digitalocean article just setup new project.
- [Harden Security of Production Project](https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project)
  - Ended up not using this one. Did refrence them quite a bit though. They used python-dotenv.
  - For some reason python-dotenv would not work for me in production. Kept getting `SECRET_KEY setting must not be empty`.
    - In Gunicorn server logs it was not empty. Got the right value. On regular logs like when doing `python manage.py migrate` kept getting value `None`.
- [Setting Up Environment Variables in Django](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)
  - The path I ended up taking to setup environment variables.
  - Used django-environ instead. It worked on the first try in production.
- [SSL Securing Nginx on Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)
  - Didn't do that yet but will probably end up doing it as the next job on the list.
- [Bootstrap Docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - Used a whole ocean load for bootstrap styling documentation.
- [Udemy Django Course with Ajax and Forms Topics](https://www.udemy.com/course/mastering-django-part-1-forms-class-based-views-ajax/learn/lecture/13680906#overview)
  - This course was very helpful in setting up the forms and ajax email form submission.
  - Even though I ended up doing the form very differently.
    - I had to custom style each individual field.
    - All the error handling was custome as well.
      - Errors were getting sent as ajax so I wouldn't have to refresh the page each time it errored on submit.
      - I did get errors from django but I sent them myself with ajax.
- [Article to Setup Email Sending with Django, Digitalocean, Namecheap](https://moonbooks.org/Articles/How-to-create-and-send-an-email-with-a-django-based-website-using-namecheap-and-digitalocean-/)
  - This artical was super helpful to setup everything correctly to send email from my django app
    - I'm not sure why I needed to setup the MX and TXT, DNS records on Digitalocea because the message did get sent without them as well.
- [Basic Setup of Email in Django](https://learndjango.com/tutorials/django-email-contact-form)
  - Used this artical for setting up the django code for sending an email.
  - Forms, Views, Templates, Urls, and some Settings.
  - Did not use the email service setup part. I have my own email from namecheap.
- [Django Email Docs](https://docs.djangoproject.com/en/3.2/topics/email/)
  - Refered to the docs a bit for the send_mail() function and some other things.
- [Secure Nginx Server with Let's Encrypt on Ubuntu Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)
  - Everything worked flawlessly. No errors, or hickups whatsoever.
