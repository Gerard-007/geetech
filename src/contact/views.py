from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import ContactForm
# Create your views here.


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')
    # success_message = 'Message sent successfully'

    def form_valid(self, form):
        reponse = super().form_valid(form)
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        description = form.cleaned_data['description']
        message = form.cleaned_data['message']
        category = form.cleaned_data['category']
        subject = 'Contact email recieved from www.geetechlab.com'
        send_message = 'name: {} \n service required {} \n job description {} \n message: {} \n mobile: {}'.format(name, category, description, message, phone)
        from_email = form.cleaned_data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, send_message, from_email, recipient_list, fail_silently=False)
        return super(ContactView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Message sent successfully!"
        


# def contact(request):
#     title = 'Send us a message'
#     contact_form = contactForm(request.POST or None)
#     confirm_message = None

#     if contact_form.is_valid():
#         comment = contact_form.cleaned_data['comment']
#         name = contact_form.cleaned_data['name']
#         phone = contact_form.cleaned_data['phone']
#         subject = 'Contact email recieved from musicadence.com'
#         message = 'name: {} \n message: {} \n mobile: {}'.format(name, comment, phone)
#         from_email = contact_form.cleaned_data['email']
#         recipient_list = [settings.EMAIL_HOST_USER]
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#         title = 'Thanks'
#         confirm_message = 'Dear {} your message was sent sucessfully'.format(name)
#         contact_form = None

#     context = {'title': title, 'contact_form': contact_form, 'confirm_message': confirm_message}
#     template = 'contact.html'
#     return render(request, template, context)