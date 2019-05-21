"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from .views import index, about, blog, meet, memb, contact_f,discuss,gallery,email
from django.conf import settings
from machina.app import board
from django.contrib.auth import views as auth_views
from .models import Images
from .image import ItemSerializer,ItemSerializer1
from rest_framework import routers

from django.conf.urls.static import static
from users import views as user_views

admin.site.site_header='Walchand Meta'
admin.site.site_title='Walchand Meta'
admin.site.index_title='Walchand Meta Admin'




urlpatterns = [
    url(r'^$', index),
    url(r'^about/$',about),
    url(r'^blog/$',blog),
    url(r'^meeting/$',meet),
    url(r'^member/$', memb),
    url(r'^contact/$',contact_f),
    url(r'^discuss/$',discuss),
    url(r'^gallery/$',gallery),
    url(r'^forum/', include(board.urls)),
    path('register/', user_views.register, name='register'),

    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^send/$',email)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
