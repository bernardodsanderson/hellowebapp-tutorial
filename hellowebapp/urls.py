from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView, RedirectView
from collection import views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from collection.backends import MyRegistrationView
# {title="urls.py", lang="python", line-numbers=on, starting-line-number=45}

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail, name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$', views.edit_thing, name='edit_thing'),
    url('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    url('browse/name/', views.browse_by_name, name='browse'),
    url('browse/name/<initial>/', views.browse_by_name, name='browse_by_name'),
    url(r'^accounts/password/reset/$', password_reset, {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    url(r'^accounts/password/reset/done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name="password_reset_complete"),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_thing/$', views.create_thing, name='registration_create_thing'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
]