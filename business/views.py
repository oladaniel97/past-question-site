
from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import send_mail
from .forms import ContactForm,ContactUsForm
from .models import *
from django.db.models import Q
import random





def index(request):
    faculties = Faculty.objects.all()
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
    
    return render(request, 'index.html', {'faculties': faculties,'form': form, 'success': False})

def about(request):
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
    return render(request, 'about.html',{ 'form': form, 'success': False})

def search(request):
    query = request.GET.get('query','')
    departments = Department.objects.filter(Q(name__icontains = query))
    courses = Course.objects.filter(Q(name__icontains = query))
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
    return render(request, 'search.html', {'query':query,'departments':departments,'courses':courses, 'form': form, 'success': False})

def department(request, id):
    faculty = get_object_or_404(Faculty, pk=id)
    departments = Department.objects.filter(faculty=faculty)
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
    return render(request, 'department.html', {'faculty': faculty, 'departments': departments,'form': form, 'success': False})

def course(request, id):
    department = get_object_or_404(Department, pk=id)
    courses = Course.objects.filter(department=department)
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
    return render(request, 'course.html', {'department': department, 'courses': courses,'form': form, 'success': False})

def past_questions(request, id):
    course = get_object_or_404(Course, pk=id)
    past_questions = YearlyPQ.objects.filter(course=course)
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
    return render(request, 'past_questions.html', {'course': course, 'past_questions': past_questions,'form': form, 'success': False})

def past_details(request,id):
    past_question = get_object_or_404(YearlyPQ,pk=id)
    # past_questions = YearlyPQ.objects.filter(course=course)
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            message = forms.cleaned_data['message']
            subject = f"New message from {name}"
            body = f"From: {name} <{email}>\n\n{message}"
            from_email = 'danielolayinka97@example.com'
            recipient_list = ['your-recipient-email@example.com']
            send_mail(subject, body, from_email, recipient_list, fail_silently=False)
            return render(request, 'details.html', {'past_question': past_question, 'forms': forms, 'successes': True})
    
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
    return render(request, 'details.html',{'past_question': past_question,'form':form, 'success': False,'forms': forms, 'successes': False,})

