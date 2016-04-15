"""cmma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.flatpages import views
from cmma.views import homepage
from programs.views import program_view, program_list
from staff.views import trainer_view, trainer_list
from users.views import user_dashboard, edit_entry


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='homepage'),
    url(r'^program/$', program_list),
    url(r'^program/(?P<slug>.+?)/$', program_view),
    url(r'^staff/$', trainer_list),
    url(r'^staff/(?P<slug>.+?)/$', trainer_view),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^accounts/profile/$', user_dashboard),
    url(r'^accounts/log/add/$', edit_entry),
    url(r'^accounts/log/(?P<entry_id>.+?)/$', edit_entry),
    url(r'^(?P<url>.*/)$', views.flatpage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
