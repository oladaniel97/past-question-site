from django import template
from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import send_mail
from business.forms import ContactUsForm

register = template.Library()

@register.inclusion_tag('contact.html')
def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"Inquiry"
            body = f"from:<{email}>\n\n{message}"
            from_email = 'danielolayinka97@example.com'
            recipient_list = ['your-recipient-email@example.com']
            send_mail(subject, body, from_email, recipient_list, fail_silently=False)
            return render(request, 'index.html', { 'form': form, 'success': True})
    
    return render(request, 'index.html',{'form':form, 'success': False})