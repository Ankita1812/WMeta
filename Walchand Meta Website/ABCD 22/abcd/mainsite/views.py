from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from .models import Article,Meeting,Member,Home,About,Contact,Images,Send_Email
from .form import ContactForm,RawContactForm


def index(request):
    data=Home.objects.all()
    context = {
        'index': data,
        'current_date': datetime.now(),
        'title': 'Home'
    }
    return render(request, 'index.html', context)
def about(request):
    data=About.objects.all()
    context = {
        'about': data,
        'current_date': datetime.now(),
        'title': 'About'
    }
    return render(request, 'about.html', context)


def discuss(request):
    context = {
        'current_date':datetime.now(),
        'title':'Discuss'
    }
    return render(request, 'discuss.html', context)


def blog(request):
    populate_db()
    articles = get_articles()

    context = {
        'articles':articles,
        'current_date':datetime.now(),
        'title':'Articles'
    }
    return render(request, 'blog.html', context)


def get_articles():
    result = Article.objects.all()
    return result

def populate_db():
    if Article.objects.count() == 0:
        Article(title = 'first item', content = 'this is the first db item').save()
        Article(title = 'second item', content = 'this is the second db item').save()

def meet(request):
    populate_db1()
    meetings= get_meetings()
    context = {
        'meetings': meetings,
        'current_date': datetime.now(),
        'title': 'Meetings'
    }
    return render(request, 'meet.html', context)

def get_meetings():
    result = Meeting.objects.all()
    return result

def populate_db1():
    if Meeting.objects.count() == 0:
        Meeting(title = 'first item', content = 'this is the first  meeting').save()
        Meeting(title = 'second item', content = 'this is the second meeting ').save()

def memb(request):
    members = getdata()
    context={
        'members': members,
        'title': 'Members'
    }
    return render(request,'memb.html',context)

def getdata():
    result = Member.objects.all()
    return  result


def contact_f(request):
    my_form = RawContactForm()
    if request.method == "POST":
        my_form = RawContactForm(request.POST)
        if my_form.is_valid():
            print (my_form.cleaned_data)
            Contact.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form,
        'title': 'Contact'
    }
    return render(request, 'contact.html', context)


def gallery(request):
    images=get_images()
    context ={
        'images':images,
        'current_date': datetime.now(),
        'title':'Images'
    }
    return render(request,'gallery.html',context)

def get_images():
    result = Images.objects.all()
    return result

def email(request):
    totalSize=0
    message = Send_Email.objects.all()
    p=Send_Email.objects.count()
    print(p)
    p=p-1
    #queryset = Send_Email.objects.filter(subject__icontains='war')[:2]
    #print(queryset)
    subject = message[p].get_subject()
    k = message[p].get_message()

    #m='hhgh'
    email_from = settings.EMAIL_HOST_USER
    l=Member.objects.count()
    re= Member.objects.all()
    print(l)

    for i in range(0,l):
        re1 = [re[i].get_email()]
        print(re1)
        send_mail(subject, k, email_from, re1)


    #for attr in (re.get_email()).__dict__.items():
     #   recipient_list = attr

    context = {
        'title': 'Contact'
    }
    return render(request,'send.html',context)