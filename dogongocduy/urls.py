"""dogongocduy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from dogo import views
from dogongocduy import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'about', views.about, name='about'),
    url(r'contact', views.contact, name='contact'),
    url(r'ban-ghe', views.chair, name='ban-ghe'),
    url(r'tuong-go', views.statue, name='tuong-go'),
    url(r'sp-khac', views.another, name='sp-khac'),
    url(r'bai-viet', views.blog, name='bai-viet'),
    url(r'^$', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
