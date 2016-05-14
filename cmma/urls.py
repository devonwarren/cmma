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
from django.contrib.auth.views import login, logout, \
    password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
from django.contrib.flatpages import views
from cmma.views import homepage
from programs.views import program_view, program_list
from blog.views import blog_list
from staff.views import trainer_view, trainer_list
from users.views import user_dashboard, edit_entry, materials


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='homepage'),
    url(r'^program/$', program_list),
    url(r'^program/(?P<slug>.+?)/$', program_view),
    url(r'^blog/$', blog_list),
    url(r'^staff/$', trainer_list),
    url(r'^staff/(?P<slug>.+?)/$', trainer_view),

    # login urls
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/password/reset/$', password_reset,
        {'post_reset_redirect': '/accounts/password/reset/done/'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$', password_reset_done),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'post_reset_redirect': '/accounts/password/done/'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete),

    url(r'^accounts/profile/$', user_dashboard),
    url(r'^accounts/log/add/$', edit_entry),
    url(r'^accounts/log/(?P<entry_id>.+?)/$', edit_entry),
    url(r'^accounts/materials/$', materials),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^(?P<url>.*/)$', views.flatpage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
